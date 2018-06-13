import re
from functools import wraps


pattern = re.compile(r"(?<=\>)(\w+[\w*\s*]+)(?=\<\/)")


def html_escaper():
    def decorator(func):
        @ wraps(func)
        def wrapper(*a, **k):
            value = func(*a, **k)
            data = re.findall(pattern, value)
            if data:
                return data[0]
            else:
                raise Exception(mssg="Data isn't find")
        return wrapper
    return decorator


@html_escaper()
def escape_html_func(data):
    return data


print(escape_html_func("<div class='modal'>some text inside the div</div>"))
