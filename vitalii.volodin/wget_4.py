from abc import ABC
from abc import abstractmethod
from collections import Counter
import urllib.request
import math
import sys
import re


RE_ALPHA = "[\S\w+('-)?]+"


class IProgressBar(ABC):
    @abstractmethod
    def display_bar(self):
        pass


class ProgressBar(IProgressBar):
    def __init__(self, file_name, downloaded_content, file_size):
        self.file_name = file_name
        self.downloaded_content = downloaded_content
        self.file_size = file_size

    def display_bar(self):
        percent_progress = math.floor(self.downloaded_content/int(self.file_size) * 100)

        print('Downloading: {0}  {1}% [{2} of {3}]  {3} bytes'.format(self.file_name,
                                                                      percent_progress,
                                                                      self.downloaded_content,
                                                                      self.file_size),
              end='\r')


class DisplayProgressBar(IProgressBar):
    def __init__(self, bar):
        self.bar = bar

    def display_bar(self):
        return self.bar.display_bar()


class IDataProvider(ABC):
    @property
    def chunk_size(self):
        return 8192

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def get_file_name(self):
        pass

    @abstractmethod
    def get_file_size(self):
        pass


class HttpResponseData(IDataProvider):
    def __init__(self, url):
        self.url = url

    def get_content(self):
        request = urllib.request.Request(self.url)
        content = urllib.request.urlopen(request)
        return content

    def get_file_name(self):
        return self.url.split('/')[-1]

    def get_file_size(self):
        """
        :return: file size in bytes
        """
        file_size = self.get_content().headers.get('content-length')
        return file_size


class DataProvider(IDataProvider):
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content.get_content()

    def get_file_name(self):
        return self.content.get_file_name()

    def get_file_size(self):
        return self.content.get_file_size()


class WriteDataToFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_data(self, data):
        try:
            with open(self.file_name, 'wb') as file:
                file.write(data)
        except (IOError, OSError) as exp:
            print(exp)


class IStatistic(ABC):
    @abstractmethod
    def get_statistic_data(self):
        pass


class WordCounter(IStatistic):
    def __init__(self, content):
        self.content = content

    def split_text(self):
        data = str(self.content.read(), encoding='utf-8')
        result = re.findall(RE_ALPHA, data)
        return result

    def get_statistic_data(self):
        return len(self.split_text())


class WordStatistic(IStatistic):
    def __init__(self, content):
        self.content = content

    def split_text(self):
        data = str(self.content.read(), encoding='utf-8')
        result = re.findall(RE_ALPHA, data)
        return result

    def get_statistic_data(self):
        counter = Counter(self.split_text()).most_common(15)
        stat = {letter: count for (letter, count) in counter}
        return stat


def progress_bar(file_name, downloaded_content, file_size):
    bar = ProgressBar(file_name, downloaded_content, file_size)
    return DisplayProgressBar(bar).display_bar()


def downloading(source, file_name, file_size, data, file, progress):
    downloaded_content = 0
    while int(file_size) > downloaded_content:
        chunk = data.read(source.chunk_size)
        file.write_data(chunk)
        downloaded_content += len(chunk)
        progress(file_name, downloaded_content, file_size)


def pyget(url):
    source = HttpResponseData(url)
    file_name = DataProvider(source).get_file_name()
    file_size = DataProvider(source).get_file_size()
    data = DataProvider(source).get_content()
    result = WriteDataToFile(file_name)
    downloading(source, file_name, file_size, data, result, progress_bar)
    print('\n{} has been downloaded successfully.'.format(file_name))


def words_statistic(url):
    source = HttpResponseData(url)
    file_name = DataProvider(source).get_file_name()
    info = []

    for action in (WordCounter, WordStatistic):
        data = DataProvider(source).get_content()
        info.append(action(data).get_statistic_data())

    print('Words statistic of {}:\n\nWord Count: {}\nStatistic: {}'.format(file_name,
                                                                           info[0],
                                                                           info[1]))

if __name__ == '__main__':
    # https://www.w3.org/TR/PNG/iso_8859-1.txt
    # http://www.dsf.unica.it/~fiore/LearningPython.pdf
    url = str(sys.argv[1])
    pyget(url)
    words_statistic(url)

