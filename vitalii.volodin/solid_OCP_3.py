from abc import ABC, abstractmethod
from math import pi, sqrt


class IShape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * pi * self.radius


class Triangle(IShape):
    def __init__(self, *sides):
        self.sides = sides
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

    def area(self):
        p = sum(self.sides) / 2
        value = p * (p - self.a) * (p - self.b) * (p - self.c)

        return sqrt(value)


class Rectangle(IShape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


class AreaCalc:
    def __init__(self, shape):
        self.shape = shape

    def get_area(self):
        return self.shape.area()


def main():
    shapes = (Circle(5), Triangle(5, 7, 9), Rectangle(6, 10))

    for shape in shapes:
        shape_name = shape.__class__.__name__
        area = AreaCalc(shape).get_area()
        print('Area of {} is {:.2f}'.format(shape_name, area))


if __name__ == '__main__':
    main()