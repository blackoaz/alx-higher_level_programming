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
    def width(self) -> int:
        """getter for the width"""

        return self.__width

    @width.setter
    def width(self, width: int):
        """setter function for the width"""

        self.validate('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """a getter class for the height"""

        return self.__height

    @height.setter
    def height(self, height: int):
        """a setter for the height variable"""

        self.validate('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """a getter method for x"""

        return self.__x

    @x.setter
    def x(self, x: int):
        """a setter for x"""

        self.validate('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """a getter for y"""

        return self.__y

    @y.setter
    def y(self, y: int):
        """a setter for y"""

        self.validate('y', y, True)
        self.__y = y

    def validate(self, name: str, value: object, not_zero=False):
        """Validates the input values
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not not_zero:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Function for calculating an area of a rectangle"""

        return self.__height * self.__width

    def display(self):
        """method for displaying # shape of the rectangle
        """
        print('\n'*self.y, end='')
        for list_len in range(self.height):
            print(' '*self.x + '#'*self.width)

    def __str__(self) -> str:
        """"string method"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height
                                                                 )

    def update(self, *args):
        """args and Kwargs"""

        arg_val = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                    args + arg_val[len(args): len(arg_val)]

        elif kwargs:
            for (k, v) in kwargs.items():
                setattr(self, k, v)
