#!/usr/bin/python3
"""This is a python file with a class Base"""
import json


class Base:
    """A class base, with a private class attribute
    and a constructor
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method for encoding"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method for writing json string repr"""

        file_name = cls.__name__ + ".json"
        text = []
        if list_objs is not None:
            for item in list_objs:
                text.append(item.to_dictionary())
        with open(file_name, 'w') as f:
            return f.write(Base.to_json_string(text))
