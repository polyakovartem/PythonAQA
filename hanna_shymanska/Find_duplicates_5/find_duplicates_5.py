import os
import sys
import hashlib


def hash_file(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def find_dup(parent_folder):
    # Duplicates in format {hash:[names]}
    dups = {}
    for dir_name, sub_dirs, file_list in os.walk(parent_folder):
        print('Scanning %s...' % dir_name)
        for file_name in file_list:
            # Get the path to the file
            path = os.path.join(dir_name, file_name)
            # Calculate hash
            file_hash = hash_file(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups

def join_dicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]


def get_results(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        print('___________________')
        for result in results:
            for sub_result in result:
                print('\t\t%s' % sub_result)
            print('___________________')

    else:
        print('No duplicate files found.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                join_dicts(dups, find_dup(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        get_results(dups)
