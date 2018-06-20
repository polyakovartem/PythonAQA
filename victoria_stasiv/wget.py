import sys
import urllib.request


def count_words(text):
    total = 0
    in_word = False
    for i in text:
        if i.isalpha():
            if not in_word:
                total += 1
            in_word = True

        if not i.isalpha():
            in_word = False

    return total


if len(sys.argv) < 2:
    print("please provide the URL")
    exit()

url = sys.argv[1]

with urllib.request.urlopen(url) as f:
    html = f.read().decode()
    print("Statistics:")
    print("The amount of words is:", count_words(html))


