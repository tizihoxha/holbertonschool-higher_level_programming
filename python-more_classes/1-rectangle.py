#!/usr/bin/python3
"""Task 1"""


def __init__(self, width =0, height=0):
    """class Rectangle that defines a rectangle"""

    self.width = width
    self.height = height

    @property:
        def width(self):
            return (self.__width)

    @width.setter:
        def width(self, value):
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
    @property:
        def height(self):
            return (self.__height)


    @height.setter:
        def height(self, value):
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("Height must be >= 0")
