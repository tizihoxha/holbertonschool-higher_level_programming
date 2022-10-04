#!/usr/bin/python3
"""Task 1"""
import json


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
    filename = cls.__name + ".json"
    def save_to_file(cls, list_objs):
        with open(filename, "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_l = [i.to_dictionary for i in list_objs]
                f.write(Base.to_json_string(dict_l))
