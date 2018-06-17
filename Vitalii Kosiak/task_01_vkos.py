"""
This module describes a homework related to homework with decorators.
"""

__author__ = 'Vitalii Kosiak'



def esc_html (func) :
    """
    Describe for function.
    ...
    Describe for function.
    """
    def wrap(*args, **kwargs) :
        map_html ={
        '&': '&amp;',
        '"': '&quot;',
        '<': '&lt;',
        '>': '&gt;'}
        new_str = ''
        str_for_esc = func(*args, **kwargs)
        
        for i in str_for_esc :
            if i in map_html :
                new_str += map_html[i]
            else :
                new_str += i
        return new_str
    return wrap

@esc_html
def inp_html (str_html):
    """
    Describe for function.
    ...
    Describe for function.
    """
    return(str_html)

test_str = '<html lang="ru" id="facebook" class="no_js"> <head><meta charset="utf-8" /><meta name="referrer" content="origin-when-crossorigin" id="meta_referrer" />'
for a in range(0,5):
    print(' ')
print('Input in function is:  ')
print(test_str)
print('Output fron funtion is: ')
print(inp_html(test_str))








########################################################
########################################################
########################################################
def esc_html2v (func) :
    """
    Describe.
    """
    def wrap(a) :
        
        new_str = ''
        str_for_esc = func(a)
        
        for i in str_for_esc :
            if i in map_html :
                new_str += map_html[i]
            else :
                new_str += i
        return new_str
    return wrap
########################################################
