#!/usr/bin/python3
"""
Returns list of attributes and methods
"""


def lookup(obj):
    """
    returns list of attrributes and methods of an obj
    """
    return [attr for attr in dir(obj)]
