from functools import wraps

def decorate_html(tag):
    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            html_text = func(*args, **kwargs)
            return "<{0}>{1}</{2}>".format(tag, html_text, tag)
        return func_wrapper
    return decorator
