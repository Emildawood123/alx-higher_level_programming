#!/usr/bin/python3
alpha = 97
while(alpha < 123):
    if alpha == 101 or alpha == 113:
        alpha += 1
        continue
    print(chr(alpha), end='')
    alpha = alpha + 1
