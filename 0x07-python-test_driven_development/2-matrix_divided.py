#!/usr/bin/python3
def matrix_divided(matrix, div):
    for n in matrix:
        if (type(n) != list):
            raise TypeError("""matrix must be a matrix \
(list of lists) of integers/floats""")
        for s in n:
            if(type(s) != float and type(s) != int):
                raise TypeError("""matrix must be a matrix \
(list of lists) of integers/floats""")
    general = len(matrix[0])
    for n in matrix:
        if(len(n) != general):
            raise TypeError("Each row of the matrix must have the same size")
    big_arr = []
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for n in matrix:
            arr = []
            for s in n:
                arr.append(round(s / div, 2))
            big_arr.append(arr)
    return (big_arr)
