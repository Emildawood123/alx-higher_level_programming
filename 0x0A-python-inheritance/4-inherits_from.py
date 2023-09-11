#!/usr/bin/python3
"""class"""


def inherits_from(obj, a_class):
    """class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
