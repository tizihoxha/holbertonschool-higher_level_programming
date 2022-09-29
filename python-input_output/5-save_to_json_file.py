#!/usr/bin/python3
"""Task 5"""


def save_to_json_file(my_obj, filename):
    """function that writes an Obj to a text file, using a JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (json.dumps(my_obj, f))
