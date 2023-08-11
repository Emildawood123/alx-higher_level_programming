#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list)
    for x in my_list:
        print("{}".format(my_list[i - 1]))
        i -= 1
