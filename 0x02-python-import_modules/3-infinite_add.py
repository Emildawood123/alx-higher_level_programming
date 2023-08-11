#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    res = 0
    if (len(sys.argv) == 1):
        print(0)
    else:
        for i in sys.argv:
            if (count == 0):
                count += 1
                continue
            res += int(sys.argv[count])
        print("{}".format(res))
