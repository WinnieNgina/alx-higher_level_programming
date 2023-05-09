#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number
while (last_digit > 10 and number > 0):
    last_digit %= 10

while (last_digit < -10 and number < 0):
    last_digit %= -10
if (last_digit > 5):
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif (last_digit != 0 and last_digit < 6):
    print(f"Last digit of {number} is {last_digit}", end=' ')
    print(f"and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
