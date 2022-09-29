#!/usr/bin/python3
"""Task 1"""


def write_file(filename="", text=""):
    """writes a string to a text file returns the number of characters"""
    nr_lines = 0
    with open(filename, 'r', encoding="utf-8") as f:
        for nr_lines in f:
            nr_lines = nr_lines + 1
        print(nr_lines)
