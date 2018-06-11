dict_with_tags = {'&': '&amp;',
                  '"': '&quot;',
                  '<': '&lt;',
                  '>': '&gt;'}


def html_escaper(func):
    """
    Decorator function which escape HTML tags
    :param func: (function)
    :return: text with escaped HTML-tags
    """
    def wrapper(*args, **kwargs):
        input_text = func(*args, **kwargs)
        return ''.join(
            [dict_with_tags[x] if x in dict_with_tags
             else x for x in input_text])
    return wrapper


@html_escaper
def html_text(input_text):
    """
    This function escape html tags
    """
    return input_text


print(html_text("<div class='modal'>some text inside the div</div>"))
