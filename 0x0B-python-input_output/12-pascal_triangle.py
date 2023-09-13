#!/usr/bin/python3
"""class"""


def pascal_triangle(n):
    """new"""
    st = []
    my_list = []
    if (n <= 0):
        return []
    stan_arr = []
    for i in range(0, n):
        for ele in range(0, i + 1):
            if (ele == 0 or ele == (i)):
                my_list.append(1)
            else:
                my_list.append(stan_arr[ele] + stan_arr[ele - 1])
        st.append(my_list)
        stan_arr = my_list
        my_list = []
    return (st)
