import hashlib
import os
import sys

from collections import defaultdict


def md5_hash(file_path, blocksize=1024):
    """Creates MD5 hash for given file.

    Args:
        file_path (str): Path to file.

    Returns:
        str: MD5 hash for given file.

    """
    try:
        hasher = hashlib.md5()

        with open(file_path, 'rb') as file:
            buffer = file.read(blocksize)

            while len(buffer) > 0:
                hasher.update(buffer)
                buffer = file.read(blocksize)

        return hasher.hexdigest()

    except (OSError, IOError, PermissionError):
        print('Cannot read file {}.'.format(file_path))
        return None


def file_hashes(path):
    """Lists files hashes in given directory and all its subdirs.

    Args:
        path (str): Path to directory.

    Returns:
        dict({<hash> : <list_of_duplicates>}): All files duplicates.

    Note: if file has no duplicates - len(<list_of_duplicates>) == 1

    """
    duplicates = defaultdict(list)

    for dirpath, subdirs, filenames in os.walk(path):

        for filename in filenames:
            path = os.path.join(dirpath, filename)
            file_hash = md5_hash(path)

            duplicates[file_hash].append(path)

    return duplicates
