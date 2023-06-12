#!/usr/bin/python3

"""
Creates empty class
"""


class BaseGeometry:
    """
    Creates class BaseGeometry:
        args:
            def area(self) - computes area
    """
    def area(self):
        """
        Computes area of geometry
        """
        raise Exception("area() is not implemented")
