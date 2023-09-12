#!/usr/bin/python3
"""class"""


def read_file(filename=""):
    """class"""
    with open(filename, "r") as file:
        read = file.read()
        print(read)
