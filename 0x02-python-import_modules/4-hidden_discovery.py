#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    dirs = dir(hidden_4)
    for direc in dirs:
        if direc[0:2] != '__':
            print("{}".format(direc))
