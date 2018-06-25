import urllib.request
from collections import Counter


class FileDownload:
    def __init__(self, file_url):
        self.file_url = file_url

    def download(self):
        try:
            filedata = urllib.request.urlopen(self.file_url)
            data = filedata.read()
            return data.decode('UTF-8')
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
    file = FileDownload('https://www.sample-videos.com/text/Sample-text-file-10kb.txt')
    data_f = file.download()
    words_l = WordList(data_f).word_list()
    words_c = CountWords(words_l).count_words()
    word_stat = WordsStatistics(words_l).word_statistics()
    print('File {} contains {} words'.format(file.file_url, words_c))

    word = input('Please enter word to check the statistics or press enter'
                 ' if you want to see the statistics of all words:\n')
    if word != '':
        single_stat = SingleWordStatistics(word_stat, word).single_word_stat()
        print('Word {} repeats {} times'.format(word, single_stat))
    else:
        print('\nBelow is a statistics of words in file {}: \n{}'.format(file.file_url, word_stat))


if __name__ == '__main__':
    main()




