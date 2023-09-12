#!/usr/bin/python3
"""class"""


def write_file(filename="", text=""):
    """class"""
    with open(filename, "w", encoding="utf-8") as file:
        return(file.write(text))