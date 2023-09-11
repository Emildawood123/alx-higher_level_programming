#!/usr/bin/python3
"""moudle"""


def add_attribute(obj, name, value):
    """class"""
    if (type(obj) == str or type(obj) == int):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
