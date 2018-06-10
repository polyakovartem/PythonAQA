def add_tags(fn):
    def wrapper(text, *tag_one, **kwargs):
        for i in range(len(tag_one)):
            text = "<{0}>{1}</{0}>".format(tag_one[i], text)
        return text
    return wrapper


@add_tags
def return_text_with_tags(text, *tag_one, **kwargs):
    return text