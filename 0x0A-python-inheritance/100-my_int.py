#!/usr/bin/python3
"""class"""


class MyInt:
    """class"""
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return ("{}".format(self.num))

    def __eq__(self, other):
        if (self.num == other):
            return False
        else:
            return True
