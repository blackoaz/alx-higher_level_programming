#!/usr/bin/python3
"""module for creating a student file"""


class Student:
    """class for student"""

    def __init__(self, first_name, last_name, age):
        """constructor for class student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method for retrieving a dictionary"""

        my_dict = dict()
        if type(attrbs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict

        return self.__dict__.copy()
