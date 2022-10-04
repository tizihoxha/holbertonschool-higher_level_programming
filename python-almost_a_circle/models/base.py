#!/usr/bin/python3
"""Task 1"""
import json
import os


class Base:
    """class Base created"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        with open(F"{cls.__name__}.json", "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_l = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dict_l))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == "[]":
            return ("[]")
        else:
            return (json.loads(json_string))
