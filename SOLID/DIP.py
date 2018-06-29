#before depending on concrete classes
'''
class Ebook_Reader():
    def __init__(self, pdf_book): 
        self.pdf_book = pdf_book
        
    def read(self):
        self.pdf_book.read()
        
class Pdf_Book:
    def read(): pass
'''

#after modification
class E_book():
    def read(): pass
    
class E_book_Reader():
    def __init__(self, e_book): 
        self.e_book = e_book
        
    def read(self):
        self.ebook.read()
        
class Pdf_Book(e_book):
    def read(): pass
    
class Doc_Book(e_book):
    def read(): pass
