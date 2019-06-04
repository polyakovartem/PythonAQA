import re
import sys
import urllib.request
from collections import Counter


# file_url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"

pattern = re.compile(r"[a-zA-Z_]+")


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
        statistic = Counter(splitted_data).most_common(10)
        return statistic


def check_argv(argument):
    if len(sys.argv) >= 2:
        return argument
    else:
        raise Exception(
            mssg='pass the arguments into command line')


def open_html_file(url):
    try:
        with urllib.request.urlopen(url) as f:
            html = f.read().decode(encoding='UTF-8')
            return html
    except (OSError, RuntimeError):
        print("Error: File does not appear to exist.")
        return []


def main():
    URL = check_argv(sys.argv[1])
    data = open_html_file(URL)
    count = WordCount(data).get_count()
    statistic = dict(WordStatistics(data).get_statistic())
    print("Url:{}\ncontains words: {},\nmost ten common"
          " of them is:{}".format(URL, count, statistic))


if __name__ == '__main__':
    main()
