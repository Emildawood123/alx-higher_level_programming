#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if (len(sys.argv) == 1):
        print("0 arguments.")
    elif len(sys.argv) == 2:
        count += 1
        print("{} argument:\n{}: {}".format(count, count, sys.argv[count]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in sys.argv:
            if (count == 0):
                count += 1
                continue
            print("{}: {}".format(count, sys.argv[count]))
            count += 1
