#!/usr/bin/python3
"""Task 10"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_dict = {}
            for el in attrs:
                if el in self.__dict__:
                    new_dict[el] = self.__dict__[el]
            return new_dict
        return (self.__dict__)
