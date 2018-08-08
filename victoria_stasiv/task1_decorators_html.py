def decorator(target_function):
    def wrapper(*args):
        value = target_function(*args)
        #escape html
        value = value.replace("&", '&amp;')
        value = value.replace('>', '&gt;')
        value = value.replace('<', '&lt;')
        value = value.replace('"', '&quot;')
        return value
    return wrapper

@decorator
def link_function(url):
    return '<a href="' + url + '">' + url + '</a>'

#print(link_function) #-> <function link_function at ...>
#print(link_function("youtube.com")) #-> <a href="youtube"..

#link_function = decorator(link_function)
#print(link_function)

print(link_function("google.com"))
print(link_function("github.com/hello&goodbye"))
