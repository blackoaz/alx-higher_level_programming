#!/usr/bin/python3
"""
base geometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from basegeometry"""

    def __init__(self, width, height):
        """constructor method"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
