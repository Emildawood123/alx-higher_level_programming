#!/usr/bin/python3
def weight_average(my_list=[]):
    res = 0
    div = 0
    if len(my_list) == 0:
        return 0
    else:
        for i in my_list:
            multi = 1
            for j in range(0, len(i)):
                if j == 1:
                    div += i[j]
                multi *= i[j]
            res += multi
    return res / div
