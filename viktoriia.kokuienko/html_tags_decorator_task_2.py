from functools import wraps

def add_div_tag(func):
    @wraps(func)
    def wrapped(input_text, *args, **kwargs):
        return "<div>" + func(input_text) + "</div>"
    return wrapped

def add_bold_tag(func):
    @wraps(func)
    def wrapped(input_text, *args, **kwargs):
        return "<b>" + func(input_text) + "</b>"
    return wrapped

@add_div_tag
@add_bold_tag
def add_tags(input_text):
    return input_text


