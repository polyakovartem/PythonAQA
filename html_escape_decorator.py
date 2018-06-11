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
