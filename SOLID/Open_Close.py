
class Rectangle: 
 
    def __init__(self, width=0, height=0): 
        self.width = width 
        self.height = height 
 
    def area(self): 
        return self.width * self.height 
 
 
shape = Rectangle(2, 5) 
 
def name(): 
    return "I'm a rectangle" 
 
shape.name = name 
print (shape.name()) # Prints: I’m a rectangle


def square_area(self): 
    return self.width ** 2 
 
Rectangle.area = square_area #!!!
square = Rectangle(2, 5) 
 
print (square.area()) # Prints 4!
