import os
import sys
import hashlib


def md5_hashed_file(path):
    hasher = hashlib.md5()
    try:
        with open(path, 'rb') as file:
            hasher.update(file.read())
    except (OSError, IOError) as exp:
        print(exp)

    return hasher.hexdigest()


def indexing(path):
    """
    Function returns dictionary which contains all pairs of 'path': 'md_5_hash' values in specified folder
    :param path: absolute path to the folder
    :return: (dict)
    """
    indexing_files = {}

    for content in os.scandir(path):
        if content.is_file():
            hashed_file = md5_hashed_file(content)
            indexing_files[content.path] = hashed_file
        elif content.is_dir():
            sub_folder = indexing(content.path)
            indexing_files.update(sub_folder)

    return indexing_files


def group_file_by_hash(index):
    grouped_files = {}

    for key, value in index.items():
        if value not in grouped_files.keys():
            grouped_files[value] = [key]
        else:
            grouped_files[value].append(key)

    return grouped_files


def find_duplicates(groups):
    duplicates = {key: value for key, value in groups.items() if len(value) > 1}
    return duplicates


def scanner(duplicates):
    if duplicates:
        print('Duplicate Files')
        for key, value in duplicates.items():
            print('Hash: {}'. format(key))
            print('Files: {}'.format(list(map(lambda file: file.split('/')[-1], value))))
    else:
        print('No duplicate files found.')


def main():
    path = str(sys.argv[1])
    index = indexing(path)
    grouped_files = group_file_by_hash(index)
    duplicates = find_duplicates(grouped_files)
    scanner(duplicates)


if __name__ == '__main__':
    main()
