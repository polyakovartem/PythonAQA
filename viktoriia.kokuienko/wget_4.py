import urllib.request
import re
from collections import Counter


class ReadHtml:
    def get_text(self):
        with urllib.request.urlopen(self.url) as html_file:
            html_text = html_file.read().decode('utf-8')
            self.html_text = html_text
            return html_text


class WordsNumber:
    def count_words(self):
        found_words = re.findall(r"[\w']+", self.html_text)
        self.found_words = found_words
        return len(found_words)


class WordStatistics:
    def calculate_statistics(self):
        statistics = Counter(self.found_words).most_common()
        return statistics


class HtmlFile(ReadHtml, WordsNumber, WordStatistics):
    def __init__(self, url):
        self.url = url


html_file = HtmlFile("https://en.wikipedia.org/wiki/Object-oriented_programming")
html_file.get_text()
print(html_file.count_words())
print(html_file.calculate_statistics())
