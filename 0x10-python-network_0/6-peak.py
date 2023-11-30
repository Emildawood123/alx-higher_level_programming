#!/usr/bin/python3
"""function"""
from helperFile import merge_sort


def find_peak(list_of_integers):
    """function"""
    length = len(list_of_integers)
    list_of_integers = merge_sort(list_of_integers, 0, length - 1)
    return list_of_integers[-1]
