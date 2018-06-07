
SYMBOLS_TO_ESCAPE = {"<":"&lt;",
					 ">":"&gt;",
					 "&":"&amp;",
					 "\"":"&quot;"}

def escape_html_tags(html_line):
	escaped_line = ""
	for symbol in html_line:
		if symbol in SYMBOLS_TO_ESCAPE:
			escaped_line += SYMBOLS_TO_ESCAPE[symbol]
		else:
			escaped_line += symbol
	return escaped_line

print(escape_html_tags("$@<-asdf>&"))