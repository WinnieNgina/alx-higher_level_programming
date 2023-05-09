#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Last_digit = abs(number) % 10
if number < 0:
    Last_digit = -Last_digit
if Last_digit > 5:
    print(f"Last digit of {number:d} is {Last_digit:d}  and is greater than 5")
elif Last_digit == 0:
    print(f"Last digit of {number:d} is {Last_digit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {Last_digit:d} and is less than 6 and not 0")
