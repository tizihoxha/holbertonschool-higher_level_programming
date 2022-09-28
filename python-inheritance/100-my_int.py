#!/usr/bin/python3
"""Task 12"""


class Myint(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        return (self.real != value)
    def __ne__(self, value):
        return (self.real == value)
