import collections


def escape_html(func):
    """""
    Task 1
    Escape HTML tags decorator object
    input: text with HTML tags
    output: text with escaped HTML tags
    """""
    def wrapper(*args, **kwargs):
        string = func(*args, **kwargs)

        escaped_string = ''
        tags = collections.OrderedDict()
        tags['&'] = '&amp;'
        tags[""] = '&quot;'
        tags['<'] = '&lt;'
        tags['>'] = '&gt;'

        for symbol in string:
            if symbol in tags:
                escaped_string = escaped_string + tags[symbol]
            else:
                escaped_string = escaped_string + symbol
        return escaped_string
    return wrapper


@escape_html
def html_input(html_string):
    return html_string


def test_escaping():
    input_text = '<div class="demo-container"><div class="demo-box">Demonstration Box</div><ul><li>list item 1</li>' \
                                                                  '<li>list <strong>item</strong> 2</li></ul></div>'
    print(html_input(input_text))


test_escaping()