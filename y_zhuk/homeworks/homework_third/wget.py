import re
import sys
import urllib.request
from abc import abstractmethod


class Preparation(object):

    @abstractmethod
    def check_argv(self, argument):
        pass


class Wget(Preparation):

    def check_argv(self, argument):
        if len(sys.argv) >= 2:
            return argument
        else:
            raise Exception(
                mssg='pass the arguments into command line')

    @staticmethod
    def count_words(text):
        count = len(re.findall("[a-zA-Z_]+", text))
        return count

    @staticmethod
    def open_html_file(url):
        try:
            with urllib.request.urlopen(url) as f:
                html = f.read().decode(encoding='UTF-8')
                print("This page has:", Wget.count_words(html), "words.")
        except (OSError, RuntimeError):
            print("Error: File does not appear to exist.")
            return []


def main():
    wget = Wget()
    html = wget.check_argv(sys.argv[1])
    wget.open_html_file(html)


if __name__ == '__main__':
    main()
