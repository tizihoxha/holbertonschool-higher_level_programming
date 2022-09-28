#!/usr/bin/python3
"""Task 12"""


class Myint(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        return (int.__ne__(self, other)
    def __ne__(self, other):
        return (not self == other)
