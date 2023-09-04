#!/usr/bin/python3
import sys
"""sys module"""
if (len(sys.argv) != 2):
    print("Usage: nqueens N")
    exit(1)
try:
    int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if (int(sys.argv[1]) < 4):
    print("N must be at least 4")
    exit(1)
for n in range(2, int(sys.argv[1])):
    mat = []
    m = -1
    for l in range(0, int(sys.argv[1])):
        m += n
        small_arr = []
        small_arr.append(l)
        tar = (int(sys.argv[1]) + 1)
        if (m > int(sys.argv[1])):
            m = m - tar
        small_arr.append(m)
        mat.append(small_arr)
    print(mat)
