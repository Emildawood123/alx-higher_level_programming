#!/usr/bin/python3
"""class"""


def read_file(filename=""):
    """class"""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
