#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    while number > 10:
        number = number % 10
    print(f"{number}", end='')
    return(number)
