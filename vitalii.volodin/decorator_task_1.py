def escape_tag(func):
    """
    Decorator function which escape HTML tags
    :param func: (function)
    :return: text with escaped HTML-tags
    """
    def wrapper(*args, **kwargs):
        string = func(*args, **kwargs)

        char = {
            '"': "&quot;",
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;'
        }

        return ''.join([char[x] if x in char else x for x in string])
    return wrapper


@escape_tag
def text(tagged_string):
    return tagged_string


def main():
    data = '<html><body><h2>Size Attributes</h2><p>Images in HTML have a set of "size" attributes,' \
           'which "specifies" the width & height of the image:</p><h1>Hello & Welcome</h1>'
    print(text(data))


if __name__ == '__main__':
    main()

