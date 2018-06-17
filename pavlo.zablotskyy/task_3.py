import math
"""
This is an example of doctest usage and SOLID principles implementation
S - Single Resposibility principle. Each class represents only one shape and methods work only with this shape
 and no other, so Square does not calculate area of Circle, etc.

"""


class Square:
    """
        Square accepts only one parameter and raises ValueError if this parameter is < 0
        get_area() returns square area
        >>> print (Square(5).get_area())
        25
        >>> print (Square(-1).get_area())
        Traceback (most recent call last):
            ...
        ValueError: Side should be greater or equal 0
    """

    def __init__(self, side_a):
        if side_a < 0:
            raise ValueError("Side should be greater or equal 0")
        self.side_a = side_a

    def get_area(self):
        return self.side_a * self.side_a


class Rectangle:
    """
        Rectangle accepts two parameters and raises ValueError if at least one of them is < 0
        get_area() returns rectangle area
        >>> print (Rectangle(5, 6).get_area())
        30
        >>> print (Rectangle(5, 0).get_area())
        0
        >>> print (Rectangle(-5, 6).get_area())
        Traceback (most recent call last):
            ...
        ValueError: Side should be greater or equal 0
    """

    def __init__(self, side_a, side_b):
        if side_a < 0 or side_b < 0:
            raise ValueError("Side should be greater or equal 0")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

class Triangle:
    """
       Triangle accepts three parameters and raises ValueError if at least one of them is < 0
       get_area() returns triangle area
       >>> print (Triangle(5, 6, 7).get_area())
       9.0
       >>> print (Triangle(-5, 6, 7).get_area())
       Traceback (most recent call last):
           ...
       ValueError: Side should be greater or equal 0
    """
    def __init__(self, side_a, side_b, side_c):
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise ValueError("Side should be greater or equal 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.side_a + self.side_b + self.side_c)/2

class Circle:
    """
       Circle accepts one parameter and raises ValueError if it is < 0
       get_area() returns circle area
       >>> print (Circle(10).get_area())
       314.1592653589793
       >>> print (Circle(-5).get_area())
       Traceback (most recent call last):
           ...
       ValueError: Radius should be greater or equal 0
    """
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius should be greater or equal 0")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius
"""
shapes = (Square(5), Rectangle(5, 6), Triangle(5, 6, 7), Circle(5))

for shape in shapes:
    print(shape.get_area())
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()