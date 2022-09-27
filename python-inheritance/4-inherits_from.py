#!/usr/bin/python3
"""Task 4"""


def inherits_from(obj, a_class):
    """True if the object is an instance of a class that inherited"""
    if issubclass(type(obj), a_class or type(obj) is a_class):
        return (True)
    else:
        return (False)
