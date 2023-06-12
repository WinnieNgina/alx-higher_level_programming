#!/usr/bin/python3
"""function that adds a new attribute to an object"""


def add_attribute(obj, attribute, value):
    """
    The __dict__ attribute is present in most objects
    Attribute allows the addition of new attributes.i

    Args:
        obj (any): The object to add an attribute to.
        attribute (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
