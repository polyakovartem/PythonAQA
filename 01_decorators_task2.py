# HTML tags Decorator. Implement as abstract as possible to be able to add new HTML tags quickly
# # input: to be or not to be, that is the question
# # output: <div><b>to be or not to be, that is the question</b></div>

input_text = "to be or not to be, that is the question"
# input_text = input("Input your text: ")

html_open_tags_list = ["<div>", "<b>"]
html_close_tags_list = []

for item in html_open_tags_list:
    output = [x for x in item]
    output.insert(1, "\\")
    output = "".join(output)
    html_close_tags_list.append(output)

html_open_tags_list = "".join(html_open_tags_list)
html_close_tags_list.reverse()
html_close_tags_list = "".join(html_close_tags_list)


def wrap_with_tags(my_function):
    def wrapped():
        return html_open_tags_list + my_function() + html_close_tags_list

    return wrapped


@wrap_with_tags
def text_processing():
    return input_text


print(text_processing())