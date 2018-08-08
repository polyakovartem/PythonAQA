"""
This module related to homework with decorators_2.
"""

__author__ = "Myroslava Hnidets"
__email__ = "Myroslava.Hnidets93@gmail.com"


_TAG_TYPE = (('h', 'paired'),
             ('title', 'paired'),
             ('b', 'paired'),
             ('h2', 'paired'),
             ('hr', 'unpaired'),
             ('link', 'unpaired'))


def convert_to_html(func_to_wrap):
        def wrapper(user_input, tag_name):

            input = func_to_wrap(user_input, tag_name)
            for tag in _TAG_TYPE:

                if tag_name in tag:
                    if tag[1] == 'paired':
                        return '<{0}>{1}</{0}>'.format(tag_name, input)
                    elif tag[1] == 'unpaired':
                        return '<{} {}>'.format(tag_name, input)
            else:
                return "Tag is not available or doesn't exist."

        return wrapper


@convert_to_html
def text_to_html(user_input, tag_name):
    return user_input


print(text_to_html('Some title', 'title'))
print(text_to_html('rel="stylesheet" href="http:///mysite.com"', 'link'))
