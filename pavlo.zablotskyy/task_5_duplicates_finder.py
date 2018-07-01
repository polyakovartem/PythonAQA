import hashlib
import os
from os import listdir
from os.path import isfile, join
import time

BUF_SIZE = 65536

"""
    DuplicatesFinder class provides ability to find all files in provided folder path,
    calculate files md5 hashes and group files with identical hashes
"""

class DuplicatesFinder:

    def __init__(self, path):
        self.start_directory = path
        self.files_list = []
        self.files_hashes = {}
        self.rev_files_hashes = {}
        self.files_with_same_hash = []

    def get_files_list(self):
        for path, subdirs, files in os.walk(self.start_directory):
            for name in files:
                self.files_list.append(os.path.join(path, name))

    # Calculates md5 hash for each file in self.files_list ans saves filename:hash in self.files_hashes
    def get_files_hashes(self):
        for file in self.files_list:
            md5 = hashlib.md5()

            try:
                with open(file, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        md5.update(data)
                self.files_hashes[file] = md5.hexdigest()
            except (PermissionError, OSError) as e:
                print(e)

    # Groups files with identical hashes
    def find_duplicates(self):
        for key, value in self.files_hashes.items():
            self.rev_files_hashes.setdefault(value, set()).add(key)
        for value in [list(values) for key, values in self.rev_files_hashes.items() if len(values) > 1]:
            self.files_with_same_hash.append(value)

    # Prints filenames with identical hash
    def display_files_hashes(self):
        for files in self.files_with_same_hash:
            print(files)


finder = DuplicatesFinder("C:\\")

start = time.time()

finder.get_files_list()
finder.get_files_hashes()
finder.find_duplicates()

diff = time.time() - start

finder.display_files_hashes()

print("Processed {} files in {} seconds".format(len(finder.files_list), diff))
