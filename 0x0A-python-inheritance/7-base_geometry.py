#!/usr/bin/python3
"""
base geometry class
"""


class BaseGeometry:
    """ Base Geometry class
    """
    def area(self):
        """ Raising an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validating input values
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
