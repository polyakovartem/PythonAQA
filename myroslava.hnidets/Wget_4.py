"""
This module related to homework with wget application analog.
"""
__author__ = "Myroslava Hnidets"
__email__ = "Myroslava.Hnidets93@gmail.com"

from urllib.request import urlopen
from collections import Counter
import string
import spacy


def download_from_url(url):
    '''
    Function access website and downloads data (files, html etc.)
    :param url: path to website
    :return: unicode data
    '''
    response = urlopen(url)
    return response.read()


class DataProcessing:
    '''
    Class takes unicode data, preprocess it (converts it into string object,
    lemmatize its content, remove stop words) and uses it for word statistic.
    :param raw_data: unicode data
    '''
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.nlp = spacy.load('en_core_web_sm')

    def __text_preprocessing(self):
        encoded_data = self.raw_data.decode('utf-8').replace('\n', '')
        doc = self.nlp(encoded_data)
        return [token.lemma_.strip() for token in doc if
                token.lemma_ not in string.punctuation
                and token.lemma_ not in self.nlp.Defaults.stop_words
                and len(token.lemma_.strip()) > 0]

    def __word_occurrence(self):
        return Counter(self.__text_preprocessing())

    def select_max_used(self, num):
        if num <= len(self.__word_occurrence()):
            return self.__word_occurrence().most_common(num)
        else:
            return 'Number value exceeds q-ty of unique words in data set.'

    def get_unique_word_count(self):
        return len(self.__word_occurrence())

    def language_diversity(self):
        return self.get_unique_word_count()/len(self.__text_preprocessing())

    def get_rarely_used_words(self):
        rarely_used = []
        for key, val in dict(self.__word_occurrence()).items():
            if val == 1:
                rarely_used.append(key)
        return rarely_used

    def get_word_occurrence(self, word):
        if self.__word_occurrence().get(word) is None:
            return 'Selected word is absent in data set.'
        else:
            return self.__word_occurrence().get(word)


# http://25.io/toau/audio/sample.txt
# http://erdani.com/tdpl/hamlet.txt

test_set = DataProcessing(download_from_url('http://erdani.com/tdpl/hamlet.txt'))

print(test_set.select_max_used(10))
print(test_set.get_word_occurrence(''))
