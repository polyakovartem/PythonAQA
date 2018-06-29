'''
Hometask 4

The simple analog of wget application which downloads file,
counts words and provides word statistics
'''

import urllib


download_url = 'https://www.sample-videos.com/text/Sample-text-file-10kb.txt'
path_to_save = '/home/vasya/Downloads/sample.txt'


def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        print('File has been dowloaded!')
    except Exception:
        print("Can't download file")


def file_statistics(path):
    
    with open(path, 'r') as a_file:
        text = a_file.read()
        
    word_list = text.replace('\n', ' ')
    word_list = word_list.split()
    words = len(word_list)
    print('The number of words in file is:', words)

    word_counter = {}
    word_list = text.replace(',', ' ').replace('.', ' ').replace(';', ' ')
    word_list = word_list.lower().split()
    for word in word_list:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] = word_counter[word] + 1

                
    print('{:15}{:5}'.format('Word','Count'))
    print('-' * 20)
    
    for  (word,occurance)  in word_counter.items():
        print('{:15}{:5}'.format(word,occurance))



download_file(download_url, path_to_save)
file_statistics(path_to_save)
