import os
import hashlib
import time


def execution_time(fn):
    def custom_wrapper(arg):
        start_executing_time = time.time()
        fn(arg)
        t = time.time() - start_executing_time
        print("Execitoin time: {} seconds".format(round(t, 4)))

    return custom_wrapper


def get_hash(filename, hash=hashlib.sha1):
    hashobj = hash()

    with open(filename, 'rb') as fp:
        hashobj.update(fp.read())
        hashed = hashobj.hexdigest()
        return hashed


@execution_time
def find_duplicates(path):
    found_files = 0
    found_duplicates = 0
    hashes_by_size = {}
    hash_files = {}

    # Duplicates by file size
    for dirpath, dirnames, filenames in os.walk(path):

        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(full_path)
            except OSError:
                pass

            duplicate = hashes_by_size.get(file_size)
            found_files += 1

            if duplicate:
                hashes_by_size[file_size].append(full_path)
            else:
                hashes_by_size[file_size] = []  # create the list for this file size
                hashes_by_size[file_size].append(full_path)
    # Duplicates by hash
    for size, files in hashes_by_size.items():
        if len(files) < 2:
            continue

        for filename in files:
            small_hash = get_hash(filename)

            duplicate = hash_files.get(small_hash)
            if duplicate:
                print("Duplicate found:\n %s\n and\n %s" % (filename, duplicate))
                hash_files[small_hash].append(filename)
                found_duplicates += 1
            else:
                hash_files[small_hash] = []  # create the list for this hash
                hash_files[small_hash].append(filename)
    print("Found files: %s" % found_files)
    print("Found dublicates: %s" % found_duplicates)


find_duplicates('D://')
