def decorator(*tags):
    def inner_decorator(target_function):
        def wrapper(*args):
            value = target_function(*args)
            #add html tags
            for tag in tags:
                value = '<' + tag + '>' + value + '<' + '/' + tag + '>'
            return value
        return wrapper
    return inner_decorator

@decorator('b', 'div')
def html_function(text):
    return 'Message: ' + text

print(html_function('Hello'))
