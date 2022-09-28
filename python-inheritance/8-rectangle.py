#!/usr/bin/python3
"""Task 8"""


class BaseGeometry:
    """public instance method: def area(self): that raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(F"{name} must be an integer")
        if value <= 0:
            raise ValueError(F"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
