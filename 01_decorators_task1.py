import re

my_dict = {'&': '&amp;',
          '"': '&quot;',
          '<': '&lt;',
          '>': '&gt;'
           }
text = input("Enter your text: ")
answer_esc = input("Enter do you want to escape(e) or unescape(u): ")


def text_processing(decor_function):
    def processing(used_dict, input_text):
        used_dict = decor_function(used_dict)
        dict_with_values = dict((re.escape(k), v) for k, v in used_dict.items())
        pattern = re.compile("|".join(dict_with_values.keys()))
        input_text = pattern.sub(lambda m: dict_with_values[re.escape(m.group(0))], input_text)
        print(input_text)
    return processing


@text_processing
def dict_processing(my_dictionary):
    if answer_esc.lower() == 'u' or answer_esc.lower() == 'unescape':
        my_dictionary = {y: x for x, y in my_dictionary.items()}
    return my_dictionary


dict_processing(my_dict, text)
