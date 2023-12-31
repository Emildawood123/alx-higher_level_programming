#!/usr/bin/python3
"""class rectangle moudle"""

from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """height."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """height."""
        return self.__width

    @width.setter
    def width(self, value):
        """height."""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height."""
        return self.__height

    @height.setter
    def height(self, value):
        """height."""
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """height."""
        return self.__x

    @x.setter
    def x(self, value):
        """height."""
        if (type(value) != int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """height."""
        return self.__y

    @y.setter
    def y(self, value):
        """height."""
        if (type(value) != int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """height."""
        return self.width * self.height

    def display(self):
        """height."""
        for _ in range(0, self.y):
            print()
        for _ in range(0, self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """height."""
        return ("[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """height."""
        if args is not None and len(args) > 0:
            for el in range(0, len(args)):
                if (el == 0):
                    self.id = args[el]
                elif (el == 1):
                    self.width = args[el]
                elif (el == 2):
                    self.height = args[el]
                elif (el == 3):
                    self.x = args[el]
                elif (el == 4):
                    self.y = args[el]
        else:
            for i in kwargs.keys():
                setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """height."""
        return ({'x': self.__x, 'y': self.__y, 'id': 1,
                'height': self.__height, 'width': self.__width})
