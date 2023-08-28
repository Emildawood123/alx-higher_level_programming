#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    ele = 0
    new_list = []
    while (count < list_length):
        try:
            ele = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            ele = 0
        except IndexError:
            print("{}".format("out of range"))
            ele = 0
        except TypeError:
            print("{}".format("wrong type"))
            ele = 0
        finally:
            new_list.append(ele)
            count += 1
    return new_list
