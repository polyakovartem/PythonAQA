"""
This module describes a homework related to homework with decorators.
"""

__author__ = 'Vitalii Kosiak'

map_html ={
    '&amp;': '&',
    '"&quot;': '"',
    '&lt;': '<',
    '&gt;': '>'}

def esc_html (func) :
    """
    Describe.
    """
    def wrap(*args, **kwargs) :
        
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
    return(str_html)

test_str = '&amp;lt;html lang=&amp;quot;ru&amp;quot; id=&amp;quot;facebook&amp;quot; class=&amp;quot;no_js&amp;quot;&amp;gt; &amp;lt;head&amp;gt;&amp;lt;meta charset=&amp;quot;utf-8&amp;quot; /&amp;gt;&amp;lt;meta name=&amp;quot;referrer&amp;quot; content=&amp;quot;origin-when-crossorigin&amp;quot; id=&amp;quot;meta_referrer&amp;quot; /&amp;gt;'
for a in range(0,5):
    print('TEST')
print('INPUT IS  ', test_str)
print('FUNCTION OUTPUT')
print(inp_html(test_str))

