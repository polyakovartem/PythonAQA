import os
import hashlib
import string
from ctypes import windll


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter+':\\')
        bitmask >>= 1
    return drives


def get_hash(file):
    with open(file, 'rb') as f:
        md5_hash = hashlib.md5(f.read())
    md5_hashed = md5_hash.hexdigest()
    return md5_hashed


def find_dupl(dupl, skipped):
    for drive in get_drives():
        for root, dirs, files in os.walk(drive):
            for name in files:
                path = os.path.join(root, name)
                try:
                    file_hash = get_hash(path)
                    if file_hash in dupl:
                        dupl[file_hash].append(path)
                    else:
                        dupl[file_hash] = [path]
                except (PermissionError, OSError):
                    skipped.append(path)
    return dupl, skipped


def main():
    print("{} {} {}".format('Duplicated Files Hash', 10 * ' ', 'Paths'))
    duplicates = {}
    skipped_files = []

    result = find_dupl(duplicates, skipped_files)

    for key, path in result[0].items():
        if len(path) > 1:
            print("{} {}".format(key, path[0]))
            for item in path[1:]:
                print("{} {}".format(len(str(key)) * ' ', item))

    print('_'*30)
    print("The following files hasn't been scanned due to lack of the permission:")
    for item in result[1]:
            print(item)


if __name__ == '__main__':
    main()




