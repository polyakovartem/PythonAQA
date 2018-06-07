"""
This module describes a homework related to homework with decorators.
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

import re
import random
from functools import wraps

pattern = re.compile(r"[^.+>]\w+(?=<.+$)")

# task 1


def escape_html():
    """This function as a decorator function handles input text
    (as *args from function to wrap) and escaped html tags from it

    Args:
         function(func) - function to wrap

    Returns:
         match[0](str) - text, that is wrapped into html tags
    """
    def real_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            func_value = function(*args, **kwargs)
            match = re.findall(pattern, func_value)
            if match:
                return match[0]  # the result of 'findall' function is a list
            else:
                print("No match find")
        return wrapper
    return real_decorator


@escape_html()
def handle_text_html(input_data):
    """This function escape html tags from input string

    Args:
        input_data(str) - text, that need to be handled

    Returns:
        input_data(str) - text, that need to be handled
         """
    return input_data


#  task 2

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


print(handle_text_html("<f><tt>text</ttt></>"))
print(wrap_text_html("to be or not to be, that is the question"))
