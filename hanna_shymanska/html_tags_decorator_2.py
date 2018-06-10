def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator

@tags("div")
@tags("b")
def get_text(name):
    return name
print(get_text("to be or not to be, that is the question"))