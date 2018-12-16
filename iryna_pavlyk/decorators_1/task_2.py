"""
This module describes a homework related to decorators.
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

import random
from functools import wraps


tags = ["a", "li", "form", "i", "b", "aside", "iframe",
        "div", "body", "html", "ul", "h2"]  # this is abstract list with tags


def add_html_tags():
    """This function as a decorator function handles input text
    (as *args from function to wrap) and wrapped it into html tags.

    Args:
         function(func) - function to wrap

    Returns:
         output_data(str) - text, that is wrapped into html tags
    """
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            func_value = function(*args, **kwargs)
            tag_1 = random.choice(tags)  # get random tag
            tag_2 = random.choice(tags)  # get random tag
            output_data = "<{}><{}>{}</{}></{}>".format(
                tag_1, tag_2, func_value, tag_2, tag_1,)
            return output_data
        return wrapper
    return real_decorator


@add_html_tags()
def wrap_text_html(input_data):
    """This function wrap a text into html tags
    Args:
        input_data(str) - text, that need to be wrapped

    Returns:
        input_data(str) - text, that need to be wrapped
    """
    return input_data


if __name__ == '__main__':
    print(wrap_text_html("to be or not to be, that is the question"))
