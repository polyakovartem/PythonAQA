"""
This module is a homework - task 2.
"""

__author__ = 'Vitalii Kosiak'


def decorator_add_html(defunc) :
    """
    Some describe for funtion.
    """
    def wrap(*args, **kwargs):
        inp_str = defunc(*args, **kwargs)
        html_dict = {'od' : '<div>', 'ob' : '<b>', 'cb' : '</b>', 'cd' : '</div>'}
        return html_dict['od'] + html_dict['ob'] + inp_str + html_dict['cb'] + html_dict['cd']
    return wrap


@decorator_add_html
def get_inp (inp_text) :
    """
    Some describe for funtion.
    """
    return inp_text
    
print('Input is: "to be or not to be, that is the question"')
print('Output is: ')
print(get_inp('to be or not to be, that is the question'))
