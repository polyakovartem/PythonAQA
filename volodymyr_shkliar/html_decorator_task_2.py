from functools import wraps

# Task 2.
# HTML tags Decorator. Implement as abstract as possible to be able to add new HTML tags quickly.
# Input: to be or not to be, that is the question.
# Output: <div><b>to be or not to be, that is the question</b></div>.


def html_decorator(tag):

    def real_decorator(original_function):

        @wraps(original_function)
        def wrapper_function(*args, **kwargs):

            return "<{0}>{1}</{0}>".format(tag, original_function(*args, **kwargs))
        return wrapper_function
    return real_decorator


@html_decorator("div")
@html_decorator("b")
def html_doc(html_string):

    return html_string


print(html_doc("to be or not to be, that is the question."))
