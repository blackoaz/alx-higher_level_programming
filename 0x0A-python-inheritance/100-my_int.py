#!/usr/bin/python3
"""
Module for customised int object
"""


class MyInt(int):
    """
    Customised int
    """
    def __new__(cls, *args, **kwargs):
        """Instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= is now =="""
        return int(self) != other

    def __ne__(self, other):
        """== is now !="""
        return int(self) == other
