from xml.sax.saxutils import escape

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    return escape(text, html_escape_table)

print(html_escape('<a> text <a>'))