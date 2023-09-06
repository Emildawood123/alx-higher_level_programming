#!/usr/bin/python3
""" mod """


def print_square(size):
    """any"""
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        for _ in range(0, size):
            print("#" * size)
