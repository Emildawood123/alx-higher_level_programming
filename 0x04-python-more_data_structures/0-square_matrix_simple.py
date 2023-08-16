#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(0, len(matrix)):
        assist = []
        for j in range(0, len(matrix[i])):
            assist.append(matrix[i][j] ** 2)
        new.append(assist)
    return (new)
