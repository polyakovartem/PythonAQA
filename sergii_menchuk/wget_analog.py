"""
To use utility, using cmd run: python wget_analog.py file_address [word]
The utility prints number of words in the file,
statistics of [word] or the statistics of all words if [word] is not entered.
"""


import sys
from collections import Counter


class FileOpen:
    def __init__(self, file):
        self.file = file

    def file_read(self):
        try:
            with open(self.file, 'r') as f:
                file_data = f.read()
                return file_data
        except(IOError, RuntimeError):
            return ''


class WordList:
    def __init__(self, data):
        self.data = data

    def word_list(self):
        words_list = []
        for element in self.data.split():
            if element.isalpha():
                words_list.append(element)
        return words_list


class CountWords:
    def __init__(self, words):
        self.words = words

    def count_words(self):
        return len(self.words)


class WordsStatistics:
    def __init__(self, word_list):
        self.word_list = word_list

    def word_statistics(self):
        statistics = Counter(self.word_list)
        return statistics


class SingleWordStatistics:
    def __init__(self, word_list, word):
        self.word_list = word_list
        self.word = word

    def single_word_stat(self):
        w_stat = Counter(self.word_list)
        try:
            return w_stat[self.word]
        except(IOError, RuntimeError):
            return 0


def main():
    data_f = FileOpen(sys.argv[1]).file_read()
    words_l = WordList(data_f).word_list()
    words_c = CountWords(words_l).count_words()
    word_stat = WordsStatistics(words_l).word_statistics()

    print('File {} contains {} words'.format(sys.argv[1], words_c))

    while True:
        try:
            single_stat = SingleWordStatistics(word_stat, sys.argv[2]).single_word_stat()
            print('word {} repeats {} times'.format(sys.argv[2], single_stat))
            break
        except:
            print('\nBelow is a statistics of words in file {}: \n{}'.format(sys.argv[1], word_stat))
            break


if __name__ == '__main__':
    main()




