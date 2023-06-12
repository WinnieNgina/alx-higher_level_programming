#!/usr/bin/python3

"""
Creates empty class
"""


class BaseGeometry:
    """
    Creates class BaseGeometry:
        args:
            def area(self) - computes area
            def integer_validator(self, name, value) - input validator
    """
    def area(self):
        """
        Computes area of geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates input
        """
        if (not type(value) is int):
            raise TypeError("{:s} must be an integer".format(name))

        elif (value <= 0):
            raise ValueError("{:s} must be greater than 0".format(name))
