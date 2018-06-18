"""
This module describes a homework related to decorators.
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

from functools import wraps


mapping = {'&': '&amp;',
           '"': '&quot;',
           '<': '&lt;',
           '>': '&gt;'}


def escape_html():
    """This function as a decorator function handles input text
    (as *args from function to wrap) and escaped html tags from it

    Args:
         function(func) - function to wrap

    Returns:
        func_value(str) - text without html tags
    """
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            func_value = function(*args, **kwargs)
            for el in mapping:
                func_value = func_value.replace(el, mapping[el])
            return func_value
        return wrapper
    return real_decorator


@escape_html()
def handle_text_html(input_data):
    """This function escape html tags from input string using
    'escape_html' decorator function

    Args:
        input_data(str) - text, that need to be handled

    Returns:
        input_data(str) - text, that need to be handled
         """
    return input_data


if __name__ == '__main__':
    print(handle_text_html('<f><tt>text</ttt></>'))
    print(handle_text_html('<f><tt>text test</ttt></>'))
    print(handle_text_html('<f><tt>tex"t t"est text2</ttt></>'))
    print(handle_text_html('<f><tt>text& test text uui</ttt></>'))
    print(handle_text_html('<f><tt>text test 3333>3 text uui fff ddd</ttt></>'))
