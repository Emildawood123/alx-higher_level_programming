#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dicList = sorted(list(a_dictionary))
    for i in dicList:
        print("{}: {}".format(i, a_dictionary[i]))
