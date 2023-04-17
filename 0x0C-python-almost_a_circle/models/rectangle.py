#!/usr/bin/python3
"""A class rectangle that inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """A class for rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class rectangle"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getter for the width"""

            return self.__width

        @width.setter
        def width(self, width):
            """setter function for the width"""

            self.__width = width

        @property
        def height(self):
            """a getter class for the height"""

            return self.__height

        @height.setter
        def height(self, height):
            """a setter for the height variable"""

            self.__height = height

        @property
        def x(self):
            """a getter method for x"""

            return self.__x

        @x.setter
        def x(self, x):
            """a setter for x"""

            self.__x = x

        @property
        def y(self):
            """a getter for y"""

            return self.__y

        @y.setter
        def y(self, y):
            """a setter for y"""

            self.__y = y
