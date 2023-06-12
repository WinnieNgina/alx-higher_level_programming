#!/usr/bin/python3
"""
checks if obj is an instance of a class or parent class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if instance belongs to a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
