import requests
import string

url = ('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res = requests.get(url)
res.status_code == requests.codes.ok
print(res.text[:])
print(len(res.text))

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
filename = 'RomeoAndJuliet.txt'
for line in open(filename):
    for word in line.lower().split():
        word = word.strip(strip)
        if len(word) > 2:
            words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))