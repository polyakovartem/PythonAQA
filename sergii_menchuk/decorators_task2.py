def html_tagging(*tags):
    """""
    Task 2
    HTML tags Decorator. Implement as abstract as possible to be able to add new HTML tags quickly
    input: to be or not to be, that is the question
    output: <div><b>to be or not to be, that is the question</b></div>
    """""
    def decor(func):
        def wrapper(*args, **kwargs):
            input_string = func(*args, **kwargs)
            return '<{0}><{1}>{2}</{1}></{0}>'.format(tags[0],tags[1], input_string)

        return wrapper
    return decor


@html_tagging('div', 'b')
def input_text(text):
    return text


def test_text():
    text = 'to be or not to be, that is the question'
    print(input_text(text))


test_text()