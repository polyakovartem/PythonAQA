def add_tag(*tags):
    """
    Decorator function which wraps string into HTML tags
    :param tags: tag sequence
    :return: string in HTML-tags
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            string = func(*args, **kwargs)

            for tag in tags[::-1]:
                string = '<{0}>{1}</{0}>'.format(tag, string)

            return string
        return wrapper
    return decorator


@add_tag('div', 'b')
def text(data):
    return data


def main():
    data = 'to be or not to be, that is the question'
    print(text(data))


if __name__ == '__main__':
    main()
