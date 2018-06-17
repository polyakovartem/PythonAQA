#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
If we want to extend the functionality of AreaCalculator to support calculating
area of different shape, we only need to define new subtype of `Shape` and leave other code
alone without modify them.
'''
from abc import ABCMeta, abstractproperty

class Shape:
    __metaclass__ = ABCMeta

    @abstractproperty
    def area(self):
        pass

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class AreaCalculator(object):

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area
        return total


def main():
    shapes = [Rectangle(1, 6), Rectangle(2, 3)]
    calculator = AreaCalculator(shapes)

    print("The total area is: ", calculator.total_area)

if __name__ == '__main__':
    main()
