from math import pi
from abc import abstractmethod


class AreaInterface(object):

    def __init__(self):
        super(AreaInterface, self).__init__()

    @abstractmethod
    def area(self):
        pass


class Rectangle(AreaInterface):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(AreaInterface):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Square(AreaInterface):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class CalculateArea(object):

    def __init__(self, figure):
        self.figure = figure

    def calculate(self):
        return self.figure


if __name__ == '__main__':
    rect = CalculateArea(Rectangle(5, 3).area()).calculate()
    print(rect)
    sq = CalculateArea(Square(2).area()).calculate()
    print(sq)
