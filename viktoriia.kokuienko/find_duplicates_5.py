import os
import hashlib


def file_hasher(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as _file:
        hasher.update(_file.read())

    return hasher.hexdigest()


def index_folder_files(folder_path):
    """
    This function finds all files in the folder with the passed path
    and calls file_hasher() to find their hash.
    Args:
        folder_path (str): Full path to the selected folder.
    Returns:
        dict: Pathes to files in the folder and their hashes.
    """
    folder_files = []
    index_files = {}
    for root, dirs, files in os.walk(folder_path):
        for _file in files:
            folder_files.append(os.path.join(root, _file))

    for file_path in folder_files:
        hashed_file = file_hasher(file_path)
        index_files[file_path] = hashed_file
    return index_files


def find_duplicates(index_files):
    """
    This function creates a reverse dict with hash as a key
    and a list of pathes to respective files as its value and
    finds duplicate files.
    Args:
        index_files (dict): Pathes to files in the folder and their hashes.
    Returns:
        list: Pathes of duplicate files.
    """
    reverse_dict = {}
    for key, value in index_files.items():
        reverse_dict.setdefault(value, set()).add(key)
    duplicates = [values for key, values in reverse_dict.items() if len(values) > 1]
    return duplicates

index_dict = index_folder_files("/home/vsun/github_repo/BaseCamp/programming_fundamentals/homework/1_basics")
print(find_duplicates(index_dict))

