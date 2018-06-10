import re


def del_tags(fn):
    def wrapper(arg):
        return re.findall('>([\w\s]+)<', fn(arg))

    return wrapper


@del_tags
def return_text_without_tags(text):
    return text
