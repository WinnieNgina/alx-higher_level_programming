#!/usr/bin/python3
for letter in range(122, 96, -1):
    print("{}".format(chr(letter - (letter % 2) * 32)), end="")
