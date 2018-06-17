import math

class Shape:
    def area(self, list_of_shapes):
        total_area = 0
        for element in list_of_shapes:
            total_area += element.area()
        return total_area

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def area(self):
        return self.height * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * math.pi

shape = Shape()
print(shape.area([Rectangle(2, 5), Circle(8)]))

