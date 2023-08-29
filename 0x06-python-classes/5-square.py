#!/usr/bin/python3
""" Square class """
class Square:
    """ Square """
    """
    __init
    Args:
    size: size of square
    """
    def __init__(self, size=0):
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
    def my_print(self):
        s = self.__size
        i = 0
        if s == 0:
            print()
        else:
            while i < s:
                c = 0
                while c < s:
                    print("#", end="")
                    c += 1
                print()
                i += 1
    
