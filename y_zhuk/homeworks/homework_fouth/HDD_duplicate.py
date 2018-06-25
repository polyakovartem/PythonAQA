
import os

folder = 'C:\\Users\ezyurzh\Downloads'
print("All files in folder %s:" % folder)
file_list = []
for (paths, dirs, files) in os.walk(folder):
    for file in files:
        file_list.append(file)


counter = {a: file_list.count(a) for a in set(file_list) if file_list.count(a) > 1}
print(counter)
