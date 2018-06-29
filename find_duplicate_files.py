#Find duplicate files on Hard Drive

import os
import sys
import hashlib

def file_hash_calc(path, blocksize = 65536):

    with open(path, 'rb') as a_file:
        
        buf = a_file.read(blocksize)
        hasher = hashlib.md5()
        while len(buf) > 0:
            hasher.update(buf)
            buf = a_file.read(blocksize)
        return hasher.hexdigest()


def find_duplicates(parent_folder):
    
    # duplicates in format {hash:[names]}
    duplicates = {}
    for dir_name, subdirs, fileList in os.walk(parent_folder):
        print('Scanning %s...' % dir_name)
        for file_name in fileList:
            # Get the path to the file
            path = os.path.join(dir_name, file_name)
            # Calculate hash
            file_hash = file_hash_calc(path)
            # Add or append the file path
            if file_hash in duplicates:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
            #Returns a dictionary with the duplicated files
    print('--------------Scan Completed-----------------------\n')
    return duplicates


def separate_dict(dictn):
    
    duplicates_list = []
    for i in dictn:
        if len(dictn[i]) > 1:
            duplicates_list.append(dictn[i])
    return duplicates_list


def show_duplicates(dupl_list):
    
    if len(dupl_list) > 0:
        for item in dupl_list:
            print('File is duplicated {} times:'.format(len(item)))
            for x in item:
                print(x)
            print('--------------------------------------------------------------------')
    else:
        print('No duplicate files found')
        
            
test_directory = '/home/vasya/Desktop'

d = find_duplicates(test_directory)

d_list = separate_dict(d)

show_duplicates(d_list)
