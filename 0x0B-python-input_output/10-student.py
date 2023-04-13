#!/usr/bin/python3
"""Module for creating a student file
"""


class Student:
    """Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """constructor for student instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        json_dict = self.__dict__
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            json_dict = {}
            try:
                for k, v in self.__dict__.items():
                    if k in attrs:
                        json_dict[k] = v
            except KeyError:
                pass
        return json_dict
