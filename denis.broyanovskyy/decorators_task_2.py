def add_tags(fn):
    def wrapper(arg, tag_one, tag_two):
        return "<{0}><{1}>".format(tag_one, tag_two) + \
               fn(arg, tag_one, tag_two) + \
               "</{1}>/{0}>".format(tag_one, tag_two)
    return wrapper


@add_tags
def return_text_with_tags(text, tag_one, tag_two):
    return text

a = return_text_with_tags("I am Denis", "div", "a")
print(a)