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

        return self.__dict__
