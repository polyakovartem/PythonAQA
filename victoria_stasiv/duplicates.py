#Find duplicate files
#

import os
import sys

root = '.'

if len(sys.argv) > 1:
    root = sys.argv[1]

files_d = {}  #a hashtable

for path, folders, files in os.walk(root):
    for file in files:
        filename = os.path.join(path, file)
        try:
            f = open(filename, 'r+b')
        except:
            continue
        contents = f.read()
        h = hash(contents)
        if h in files_d:
            l = files_d[h]
            l.append(filename)
        else:
            files_d[h] = [filename]
        f.close()

for duplicates in files_d.values():
    if len(duplicates) > 1:
        print(duplicates)
