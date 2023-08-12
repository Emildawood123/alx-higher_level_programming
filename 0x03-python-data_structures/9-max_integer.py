#!/usr/bin/python3
def max_integer(my_list=[]):
    num = 0
    if my_list == []:
        return (None)
    for i in range(0, len(my_list)):
        if (my_list[i] > num):
            num = my_list[i]
        else:
            continue
    return (num)
