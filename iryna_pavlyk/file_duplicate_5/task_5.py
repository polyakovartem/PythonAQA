"""
Given a folder, walk through all files within the folder and subfolders
and get list of all files that are duplicates
The md5 checcksum for each file will determine the duplicates
"""

import os
import hashlib
from collections import defaultdict

working_directory = "/files"
logger = 'duplicated_files.txt'


# Write the list of duplicate files to txt file
def write_to_file(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for row in data:
                file.write(row + '\n')
    except (OSError, IOError):
        print("An Error has occurred!")


def calculate_md5(filename, chunk_size=1024):
    """
    Function which takes a file name and returns md5 checksum of the file
    """
    hash = hashlib.md5()
    with open(filename, "rb") as file:
        chunk = file.read(chunk_size)
        while chunk:
            hash.update(chunk)
            chunk = file.read(chunk_size)
    # Return the hex checksum
    return hash.hexdigest()


def find_duplicated_file():
    # The dict will have a list as values
    md5_dict = defaultdict(list)

    # Walk through all files and folders within directory
    try:
        for path, dirs, files in os.walk(working_directory):
            for file in files:
                print("Analyzing path {} to file {}".format(path, file))
                path_to_file = os.path.join(os.path.abspath(path), file)
                # If there are more files with same checksum append to list
                md5_dict[calculate_md5(path_to_file)].append(path_to_file)
    except PermissionError:
        print("Permission denied to {}".format(path_to_file))

    # Identify keys (checksum) having more than one values (file names)
    duplicate_files = (
        val for key, val in md5_dict.items() if len(val) > 1)

    for dupl_file in duplicate_files:
        write_to_file(dupl_file, logger)

    print("============ Well done!!! ============")


if __name__ == "__main__":
    find_duplicated_file()

# https://gist.github.com/vinovator/a2ba7306e829bf3a9010
