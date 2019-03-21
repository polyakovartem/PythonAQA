import requests
import re
from collections import Counter

# Task 4.
# Create analog of wget application which downloads file, counts words and provides word statistics.


def download_file(url):
    response = requests.get(url, stream=True)
    return response.text


def get_words(text):
    return [char.lower() for char in re.findall(r'\w+', text)]


def words_statistic(content):
    return Counter(get_words(content))


if __name__ == '__main__':
    url = download_file('https://www.sample-videos.com/text/Sample-text-file-50kb.txt')

    for word, occurrences in words_statistic(url).most_common():
        print(word, occurrences)
