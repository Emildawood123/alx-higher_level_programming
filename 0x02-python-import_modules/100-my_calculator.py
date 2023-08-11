#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        if (sys.argv[2] == '+'):
            print("{} + {} = {}".format(a, b, add(int(a), int(b))))
            exit(0)
        elif (sys.argv[2] == '-'):
            print("{} - {} = {}".format(a, b, sub(int(a), int(b))))
            exit(0)
        elif (sys.argv[2] == '*'):
            print("{} * {} = {}".format(a, b, mul(int(a), int(b))))
            exit(0)
        elif (sys.argv[2] == '/'):
            print("{} / {} = {}".format(a, b, div(int(a), int(b))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
