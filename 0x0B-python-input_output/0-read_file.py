#!/usr/bin/python3

""" Read a text file """


def read_file(filename=""):
    """
    Read text file
    """
    with open(filename, encoding="utf-8") as textfile:
        print(textfile.read(), end="")
