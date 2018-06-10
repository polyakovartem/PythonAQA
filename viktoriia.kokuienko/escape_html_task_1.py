from functools import wraps

escape_symbols = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
}

def escape_html(func):
    @wraps(func)
    def wrapped(html_input, *args, **kwargs):
        return func(''.join([escape_symbols.get(char, char) for char in html_input]))
    return wrapped


@escape_html
def html_output(html_input):
    print html_input
