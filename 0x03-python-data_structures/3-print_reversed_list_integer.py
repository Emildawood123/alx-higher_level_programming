#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        i = len(my_list) - 1
        for x in my_list:
            print("{:d}".format(my_list[i]))
            i -= 1
