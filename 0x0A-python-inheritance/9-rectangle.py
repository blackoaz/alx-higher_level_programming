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

    def area(self):
        """function for calculating area of a rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """string function"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
