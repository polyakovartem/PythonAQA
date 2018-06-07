from functools import wraps

def decorate_div_tag():
	def wrapper(func):
		@wraps(func)
		def div_tag(*args):
			params = func(*args)
			str = "<div>" + params + "</div>"
			return str
		return div_tag
	return wrapper


def decorate_b_tag():
	def wrapper(func):
		@wraps(func)
		def b_tag(*args):
			params = func(*args)
			str = "<b>" + params + "</b>"
			return str
		return  b_tag
	return wrapper

@decorate_div_tag()
@decorate_b_tag()
def simple_text(text):
	return text

print (simple_text("to be or not to be, that is the question"))
