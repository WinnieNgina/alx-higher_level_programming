#!/usr/bin/python3
"""
append a string to a textfile
"""


def append_write(filename="", text=""):
    """
    Append a string to a text file
    """
    with open(filename, 'a', encoding="utf-8") as textfile:
        return textfile.write(text)
