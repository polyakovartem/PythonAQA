import hashlib
import os
from collections import defaultdict

PATH = '/Users'


def generate_md5(filename, chunk_size=1024):

    try:
        hash = hashlib.md5()

        with open(filename, 'rb') as file:
            chunk = file.read(chunk_size)

            while chunk:
                hash.update(chunk)
                chunk = file.read(chunk_size)

        return hash.hexdigest()

    except (FileNotFoundError, PermissionError) as err:
        print('Could not read file:', err)


def check_duplicates(path):
    hash_dict = defaultdict(list)

    for paths, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(paths, file)

            hash_dict[generate_md5(path)].append(path)

    return hash_dict


if __name__ == '__main__':

    for key, val in check_duplicates(PATH).items():
        if len(val) > 1:
            print('{}: {}'.format(key, val))
