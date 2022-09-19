#!/usr/bin/python3
"""Task 1"""


class Square:
    """Write a class Square that defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return (self.__size**2)
