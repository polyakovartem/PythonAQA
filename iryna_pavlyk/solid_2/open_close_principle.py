"""
This module describes a homework related to SOLID.
Open/Close principle
"""
__author__ = "Iryna Pavlyk"
__email__ = "iruska.m1@ukr.net"

from math import pi, sqrt


class ShapeArea(object):
    def get_area(self, *sides):
        pass


class Circle(ShapeArea):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius ** 2


class Square(ShapeArea):
    def __init__(self, high, width):
        self.high = high
        self.width = width

    def get_area(self):
        return self.high * self.width


class Triangle(ShapeArea):
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def get_area(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        return sqrt(p * (p-self.side_1) * (p-self.side_2) * (p-self.side_3))


if __name__ == '__main__':
    print(Circle(5).get_area())
    print(Square(2, 3).get_area())
    print(Triangle(6, 7, 5).get_area())

