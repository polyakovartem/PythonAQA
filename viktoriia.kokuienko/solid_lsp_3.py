import math
from abc import ABC

class Shape(ABC):
    def __init__(self, area):
        self.area = area

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        super(Shape, self).__init__()
        self.area = self.height * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super(Shape, self).__init__()
        self.area = self.radius * self.radius * math.pi

shape = Shape(9)
print(shape.area)
rectangle = Rectangle(5, 6)
print(rectangle.area)
circle = Circle(10)
print(circle.area)


