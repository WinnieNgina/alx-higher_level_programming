#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):  # check if negative
        number *= -1

    while (number > 10):
        number %= 10

    print(f"{number:d}", end='')
    return number
