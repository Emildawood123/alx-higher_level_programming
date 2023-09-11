#!/usr/bin/python3
"""moudle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class"""
    def __init__(self, size):
        self.__size = size
        super(Square, self).integer_validator("size", size)

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        return (self.__size ** 2)
