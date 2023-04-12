#!/usr/bin/python3
"""Ädding more methods to class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area method raising exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for validating value inputs"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
