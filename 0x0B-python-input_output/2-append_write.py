#!/usr/bin/python3
"""class"""


def append_write(filename="", text=""):
    """class"""
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
