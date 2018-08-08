"""
This module relates to homework with file duplicates detecting.
"""
__author__ = "Myroslava Hnidets"
__email__ = "Myroslava.Hnidets93@gmail.com"

import os
import hashlib


def find_all_files(root_folder):
    '''
    Function finds all path + files in specified directory.
    :param root_folder: str: path to folder where to search for duplicates.
    :return: list of files from directory (path + file_name).
    '''
    files_in_folder = []

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            files_in_folder.append(os.path.join(root, file))

    return files_in_folder


def hash_file(file_name, chunk_size=1024):
    '''
    Function caches content of file.
    :param file_name: str: path + file_name of file, that need to be hashed;
           chunk_size: chunk of file to process (1024 by default).
    :return: str: hashed file content.
    '''
    hasher = hashlib.md5()

    with open(file_name, 'rb') as file_content:
        file_chunk = file_content.read(chunk_size)
        while file_chunk:
            hasher.update(file_chunk)
            file_chunk = file_content.read(chunk_size)

    return hasher.hexdigest()


def find_duplicates(folder_path):
    '''
    Function finds duplicates in folder and subfolders.
    :param folder_path: path to folder where to search for duplicated.
    :return: list with tuples where each tuple is a pair of files with the same content.
    '''
    duplicates_list = []
    all_files = find_all_files(folder_path)
    cached_dict = {}

    for file in all_files:
        cached_dict[file] = hash_file(file)

        if 1 < len(cached_dict) <= len(all_files):
            for key, file_content in cached_dict.items():
                if file != key and cached_dict[file] == file_content:
                    duplicates_list.append((file, key))

    return duplicates_list


print(find_duplicates('/home/myroslava/test_duplicates/conventions'))
