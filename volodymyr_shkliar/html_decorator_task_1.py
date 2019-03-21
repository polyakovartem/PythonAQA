from functools import wraps

# Task 1.
# Escape HTML tags decorator object.
# Input: text with HTML tags.
# Output: text with escaped HTML tags.


def html_decorator(original_function):

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        escape_string = original_function(*args, **kwargs)

        escape_string = escape_string.replace("&", "&amp;")  # Must be done first!
        escape_string = escape_string.replace("<", "&lt;")
        escape_string = escape_string.replace(">", "&gt;")
        escape_string = escape_string.replace('"', "&quot;")
        escape_string = escape_string.replace('\'', "&#x27;")

        return escape_string
    return wrapper_function


@html_decorator
def html_doc(html_string):

    return html_string


print(html_doc("<img src=\"w3schools.jpg\" alt=\"W3Schools.com\" width=\"104\" height=\"142\">"))
