#!/usr/bin/python3
for i in range(0, 100):
    if i // 10 >= i % 10:
        continue
    if i == 89:
        print("{}".format(i))
    else:
        print("%02d, " % (i), end='')
