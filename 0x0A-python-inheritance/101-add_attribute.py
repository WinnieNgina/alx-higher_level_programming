#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    """
    The __dict__ attribute is present in most objects
    Attribute allows the addition of new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
