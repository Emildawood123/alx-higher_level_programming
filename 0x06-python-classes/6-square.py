#!/usr/bin/python3
""" Square class """
class Square:
    """ Square """
    """
    __init
    Args:
    size: size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """ area """
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        return self.__size ** 2
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if (type(value[0]) != int 
            or type(value[1]) != int 
            or value[0] < 0 
            or value[1] < 0
            or type(value) != tuple
            or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
    def my_print(self):
        s = self.__size
        pos = self.__position
        i = 0
        if s == 0:
            print()
        else:
            for _ in range(0, pos[1]):
                print()
            while i < s:
                print("{}".format(" " * pos[0]), end="")
                print("#" * s,end="")
                print()
                i += 1
