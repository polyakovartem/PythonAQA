"""
This module related to homework with decorators_1.
"""
__author__ = "Myroslava Hnidets"
__email__ = "Myroslava.Hnidets93@gmail.com"


_TAGS_MAPPING = {
        '"': '&quot;',
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;'
}


def decorate_html(func):

        def wrapper(user_input):
            html_code = func(user_input)
            return html_code.translate(str.maketrans(_TAGS_MAPPING))
        return wrapper


@decorate_html
def function_to_wrap(user_input):
    return user_input


print(function_to_wrap('<h2>HTML Links</h2>'))
