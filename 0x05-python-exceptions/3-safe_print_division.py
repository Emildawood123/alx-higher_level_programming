#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return (None)
    finally:
        if b == 0:
            print("Insert result: {}".format(None))
        else:
            print("Insert result: {}".format(a / b))