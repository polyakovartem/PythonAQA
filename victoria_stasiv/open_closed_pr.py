#Correct use of open-closed principle


class ShapeCalculator:
    def calculate_area(self, shape):
        print(shape.calculate_area())


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        pi = 3.14159
        area = pi * self.radius * self.radius
        return area


class Square:
    def __init__(self, length):
        self.length = length

    def calculate_area(self):
        area = self.length * self.length
        return area


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 1/2 * self.height * self.base
        return area


co = ShapeCalculator()
co.calculate_area(Circle(5))  # ~78.5
co.calculate_area(Circle(100))  # 31415.9
co.calculate_area(Rectangle(3, 3))  # 9
co.calculate_area(Rectangle(5, 10))  # 50
co.calculate_area(Square(10))  # 100
co.calculate_area(Triangle(4, 3))  # 6
