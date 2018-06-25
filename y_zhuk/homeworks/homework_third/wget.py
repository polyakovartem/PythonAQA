import re
import sys
import urllib.request
from collections import Counter


# file_url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
# site_url = "https://habr.com"
pattern = re.compile(r"[a-zA-Z_]+")


class CheckSystemArguments:

    @staticmethod
    def check_argv(argument):
        if len(sys.argv) >= 2:
            return argument
        else:
            raise Exception(
                mssg='pass the arguments into command line')


class WorkWithHtmlFile:

    @staticmethod
    def open_html_file(url):
        try:
            with urllib.request.urlopen(url) as f:
                html = f.read().decode(encoding='UTF-8')
                return html
        except (OSError, RuntimeError):
            print("Error: File does not appear to exist.")
            return []


class WordCount:
    def __init__(self, file_content):
        self.file_content = file_content

    def get_count(self):
        count = len(re.findall(pattern, self.file_content))
        return count


class WordStatistics:

    def __init__(self, file_content):
        self.file_content = file_content

    def get_statistic(self):
        splitted_data = re.findall(pattern, self.file_content)
        statistic = Counter(splitted_data).most_common(50)
        return statistic


def main():
    URL = CheckSystemArguments.check_argv(sys.argv[1])
    data = WorkWithHtmlFile.open_html_file(URL)
    print(WordCount(data).get_count())
    print(WordStatistics(data).get_statistic())


if __name__ == '__main__':
    main()
