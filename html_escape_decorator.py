#Task 1
'''
Escape HTML tags decorator object
input: text with HTML tags
output: text with excaped HTML tags
'''

#References
'''
See example https://www.freeformatter.com/html-escape.html
'''


import html

test_string = 'Hello "XYZ" this <br> a test & so on'

def html_escape(func):

    def wrapper(param):
        return html.escape(func(param))
    return wrapper


@html_escape
def get_string(strg):
    return strg

print(get_string(test_string))
