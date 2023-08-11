#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if (len(sys.argv) == 1):
        print("0 arguments.")
    else:
        print("{} arguments:", len(sys.argv) - 1)
        for i in sys.argv:
            if (count == 0):
                count += 1
                continue
            print("{}: {}".format(count, sys.argv[count]))
            count += 1
