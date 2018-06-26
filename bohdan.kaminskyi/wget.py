import requests
import re
import sys
from collections import Counter
# https://www.sample-videos.com/text/Sample-text-file-1000kb.txt
# TODO
# -o new_name
WORD_PATTERN = r'\w+'


def get_url_from_sysargs():
    """Retrieves URL from system arguments.

    Returns:
        str: Retrieved URL.

    """
    if len(sys.argv) < 2:
        usage_notes = 'Usage: wget [options] <link>'
        print(usage_notes)
        sys.exit()
    else:
        url = sys.argv[-1]
        return url


def download_file(url):
    """Downloads file pointed by URL.

    Args:
        url (str): URL which points to a file.

    Returns:
        str: Filename of downloaded file.

    """
    local_filename = url.split('/')[-1]
    request1 = requests.head(url)
    request = requests.get(url, stream=True)
    file_size = int(request.headers['Content-length'])

    try:

        with open(local_filename, 'wb') as file:
            downloaded = 0

            for chunk in request.iter_content(chunk_size=1024):
                if chunk:
                    downloaded += len(chunk)
                    file.write(chunk)

                    done = int(50 * downloaded / file_size)
                    sys.stdout.write("\r[%s%s]" % ('=' * done, ' '*(50-done)))
                    sys.stdout.flush()

        print('\nSuccessfully downloaded {}'.format(local_filename))

    except (OSError, IOError) as error:
        print('Cannot write to file \"{}\".'.format(local_filename))
        sys.exit()

    return local_filename


def get_words(line):
    """Finds all words in given line.

    Arguments:
        line (str): Line to find words in.

    Returns:
        list: List of words in line.

    """
    return [word.lower() for word in re.findall(WORD_PATTERN, line)]


def get_words_stats(filename):
    """Shows count of each word in given file.

    Arguments:
        filename (str): File for searching words.

    Returns:
        words_counter (Counter): Count of each word in file.

    """
    words_counter = Counter()
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = get_words(line)
                words_counter.update(words)

    except (OSError, IOError) as error:
        print('Cannot write to file \"{}\".'.format(local_filename))
        sys.exit()

    return words_counter


if __name__ == '__main__':
    url = get_url_from_sysargs()
    file = download_file(url)
    word_stats = get_words_stats(file)

    print('{:15}{:3}'.format('Word', 'Count'))
    print('-' * 18)
    for word, occurrences in word_stats.most_common(15):
        print('{:15}{:3}'.format(word, occurrences))
