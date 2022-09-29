#!/usr/bin/python3
"""Task 10"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return (self.__dict__)
    if type(attrs) is a list of str:
        getattr(self.first_name, self.last_name)
    else:
        getattr(self.first_name, self.last_name, age))
