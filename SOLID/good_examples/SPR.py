'''
We split class Rectangle into two classes
'''

class Rectangle: 
 
    def __init__(self, width=0, height=0): 
        self.width = width 
        self.height = height 
 
    def area(self): 
        return self.width * self.height 
 
 
class DrawRectangle: 
    def draw(self): 
        # Do some drawing
        pass

