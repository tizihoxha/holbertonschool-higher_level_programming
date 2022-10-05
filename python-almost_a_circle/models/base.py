#!/usr/bin/python3
"""Task 1"""
import json
from os import path


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
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        with open(F"{cls.__name__}.json", "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_l = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dict_l))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returning a list of instances"""
        list_d = []
        if path.exists(F"{cls.__name__}.json"):
            with open(F"{cls.__name__}.json", "r", encoding="UTF-8") as f:
                list_json = cls.from_json_string(f.read())
                for inst in list_json:
                    list_d.append(cls.create(**inst))
                return list_d
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes CSV"""
        with open(F"{cls.__name__}.csv", "w", encoding="UTF-8") as f:
            if list_objs is not None:
                dict_l = [i.to_dictionary() for i in list_objs]
            f.write(Base.to_json_string(dict_l))

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV"""
        list_d = []
        if path.exists(F"{cls.__name__}.csv"):
            with open(F"{cls.__name__}.csv", "r", encoding="UTF-8") as f:
                list_csv = Base.from_json_string(f.read())
                for inst in list_json:
                    list_d.append(cls.create(**inst))
                return list_d
        else:
            return []

