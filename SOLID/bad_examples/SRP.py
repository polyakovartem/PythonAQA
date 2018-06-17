'''
This is an example of a violation of Single Responsibility Principle.
Given class Rectangle has two responsibilities.
'''

class Rectangle: 
     
    def __init__(self, width=0, height=0):
        self.width = width 
        self.height = height 
     
    def draw(self): 
        # Do some drawing 
        pass 
 
    def area(self): 
        return self.width * self.height
