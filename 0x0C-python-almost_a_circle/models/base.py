#!/usr/bin/python3
"""This is a python file with a class Base"""


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
