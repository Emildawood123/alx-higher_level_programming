#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number1 = number
if number1 < 0:
    number1 = number1 * -1
    while (number1 > 10):
        number1 = number1 % 10
    number1 = number1 * -1
else:
    while (number1 > 10):
        number1 = number1 % 10
if number1 < 6 and number != 0:
    print(f"Last digit of {number} is {number1} and is less than 6 and not 0")
elif number1 > 5:
    print(f"Last digit of {number} is {number1} and is greater than 5")
else:
    print(f"Last digit of {number} is {number1} and is 0")
