from functools import wraps


tags = ["div", "b"]


def add_html_tags():
    """
    This function as a decorator function handles input text and wrapped it into html tags.
    :parameter: function(func) - a function that needs to be wrapped up
    :return: text_inside_tags(str) - a text that needs to be wrapped up into tags
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*a, **k):
            input_text = func(*a, **k)
            text_inside_tags = "<{}><{}>{}</{}></{}>"\
                .format(tags[0], tags[1], input_text, tags[1], tags[0])
            return text_inside_tags
        return wrapper
    return decorator


@add_html_tags()
def wrap_text_html(input_text):
    """
    This function wrap a text into html tags
    """
    return input_text


print(wrap_text_html("to be or not to be, that is the question"))
