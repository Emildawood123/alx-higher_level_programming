#!/usr/bin/python3
""" moudle """


class Rectangle:
    """ defs """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        rec = ""
        if (self.__width == 0 or self.__height == 0):
            return ""
        else:
            for _ in range(0, self.__height):
                rec += "#" * self.__width
                rec += "\n"
            rec = rec[0:-1]
        return rec

    def __repr__(self):
        return "{}({}, {})".format(__class__.__name__, self.__width,
                                   self.__height)

    def __del__(self):
        print("Bye rectangle...")
