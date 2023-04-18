#!/usr/bin/python3
"""A class rectangle that inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """A class for rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the class rectangle"""

        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

        def type_validation(self, name:  str,
                            value: object, not_zero_less=True) -> None:
            """validation of the type and value
            """
            if not isinstance(value, int):
                raise TypeError("{} must be an integer".format(name))
            if not_zero_less:
                if value <= 0:
                    raise ValueError("{} must be > 0".format(name))

            else:
                if value < 0:
                    raise ValueError("{} must be >= 0".format(name))
