#!/usr/bin/python3
"""
returns dictionary desc for JSON serialization of an object
"""


def class_to_json(obj):
    """
    returns dictionary desc for JSON serialization of an object
    """

    return vars(obj)
