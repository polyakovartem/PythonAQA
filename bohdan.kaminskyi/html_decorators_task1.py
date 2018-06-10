import re
from functools import wraps

ESCAPE_MAP = {"<": "&lt;",
              ">": "&gt;",
              "&": "&amp;",
              "\"": "&quot;"}

TRANSLATION_TABLE = {ord(symbol): replacement for (symbol, replacement) in ESCAPE_MAP.items()}


def escape_html(func):
    @wraps(func)
    def wrapper(html, *args, **kwargs):
        return re.sub(r"\"(.*)\"", lambda x: "\"" + x.group(1).translate(TRANSLATION_TABLE) + "\"", html)
    return wrapper
