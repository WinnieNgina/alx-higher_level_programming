#!/usr/bin/python3

"""
Write a string to a text file
"""


def write_file(filename="", text=""):

    """
    Write a string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as textfile:
        return textfile.write(text)
