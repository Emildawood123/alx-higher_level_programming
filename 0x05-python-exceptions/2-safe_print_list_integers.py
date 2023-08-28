#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    count2 = 0
    while (count + count2 < my_list):
        try:
            print("{:d}".format(my_list[count + count2]), end="")
            count += 1
        except (ValueError, TypeError):
            count2 += 1
    if (count + count2 < x):
        raise  IndexError("list index out of range")
    print("".format())
    return count
