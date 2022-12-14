#!/usr/bin/python3
"""Task 5"""


class Square:
    """Write a class Square that defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size**2)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            height = self.position[0]
            width = self.position[1]
            for i in range(width):
                print("")
            for side in range(self.size):
                for j in range(height):
                    print(" ", end="")
                for side1 in range(self.size):
                    print("#", end="")
                print("")
