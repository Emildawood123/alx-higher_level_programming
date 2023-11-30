#!/usr/bin/python3
"""function"""


def find_peak(list_of_integers):
    """function"""
    diff = 0
    if (len(list_of_integers) == 0):
        return None
    else:
        for i in range(len(list_of_integers) - 1):
            if (list_of_integers[i] - list_of_integers[i + 1] >= diff):
                number = list_of_integers[i]
                diff = list_of_integers[i] - list_of_integers[i + 1]
        return number
