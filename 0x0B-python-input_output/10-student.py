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
        """Retrieving a dictionary representation of a student instance
        """

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.upate({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
