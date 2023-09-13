#!/usr/bin/python3
"""module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_list = list(self.__dict__.keys())
        d = dict()
        if (attrs is None):
            return (self.__dict__)
        for i in my_list:
            if (i in attrs):
                d[i] = self.__dict__[i]
        return (d)
