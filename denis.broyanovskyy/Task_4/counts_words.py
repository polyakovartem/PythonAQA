import urllib.request


def download_file(file_name):
    url = 'http://tululu.org/txt.php?id=51571'
    urllib.request.urlretrieve(url, file_name)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as fp:
        return fp.read()


def counts_words(text):
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].strip(".,?:;\"!()")
    return len(words)


download_file("text.txt")
print(counts_words(read_file("text.txt")))
