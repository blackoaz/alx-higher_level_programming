#!/usr/bin/python3
"""class for square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class for rectangle"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """constructor for square class"""

        super().__init__(size, size, x, y, id)

        self.__size = size

    def __str__(self):
        """string method"""

        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[square] ({:d}) {:d}/{:d} - {:d}".format(id, x, y, size)
