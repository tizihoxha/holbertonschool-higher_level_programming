#!/usr/bin/python3
"""Task 1"""


class MyList(list):
    """fuction that prints the list, but sorted ascending sort"""
    def print_sorted(self):
        print(sorted(self))
