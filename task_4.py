import collections
import re
import urllib.request


class WordsCounter:
    def __init__(self, url):
        self.url = url
        self.retrieved_file = ""
        self.words = {}
        self.pure_text = []

    def retrieve_file(self):
        """Receives file from provided during __init__ url"""
        response = urllib.request.urlopen(self.url)
        self.retrieved_file = response.read().decode('utf-8')

    def get_pure_text(self):
        self.pure_text = re.findall(r"[\w']+", self.retrieved_file)

    def get_words_amount(self):
        """Counts amount of unique words in received file"""
        for word in self.pure_text:
            self.words[word] = self.pure_text.count(word)

    def provide_statistic(self):
        """Prints words statistics in ordered by key representation"""
        sorted_dict = collections.OrderedDict(sorted(self.words.items()))
        for k, v in sorted_dict.items(): print("{} : {}".format(k, v))


counter = WordsCounter("http://bbc.com")
counter.retrieve_file()
counter.get_pure_text()
counter.get_words_amount()
counter.provide_statistic()
