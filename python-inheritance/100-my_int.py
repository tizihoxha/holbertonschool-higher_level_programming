#!/usr/bin/python3
"""Task 12"""


class Myint(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        return (sef.value == other.value)
    def __ne__(self, other):
        return (not self == other)
