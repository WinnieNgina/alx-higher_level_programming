#!/usr/bin/python3
"""
Checks if object is instance of derived from class
"""


def inherits_from(obj, a_class):
    """
    Checks if instance belongs to a derived from class
    """
    if type(obj) is a_class:
        return False

    elif isinstance(obj, a_class):
        return True

    else:
        return False
