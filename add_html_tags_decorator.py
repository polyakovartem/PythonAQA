#Task 2
'''
HTML tags Decorator. Implement as abstract as possible to be able to add new HTML tags quickly
input: to be or not to be, that is the question
output: <div><b>to be or not to be, that is the question</b></div>
'''

test_string = 'to be or not to be, that is the question'


def add_tag(*args):
    def func_decorator(func):
       def func_wrapper(text):
           s = text
           for tag in args:
               s = '<{}>'.format(tag) + s + '</{}>'.format(tag)
           return s
       return func_wrapper
    return func_decorator


@add_tag('div', 'b')
def get_text(text):
    return text

print(get_text(test_string))
