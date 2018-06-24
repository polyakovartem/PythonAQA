import requests
from string import punctuation
from operator import itemgetter

url = ('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res = requests.get(url)
res.status_code == requests.codes.ok
print(res.text[:])
print(len(res.text))

words = {}
words_gen = (word.strip(punctuation).lower() for line in open("RomeoAndJuliet.txt")
                                             for word in line.split())
for word in words_gen:
    words[word] = words.get(word, 0) + 1
top_words = sorted(words.items(), key=itemgetter(1), reverse=True)[:]
for word, frequency in top_words:
    print("%s %d" % (word, frequency))