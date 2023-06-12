#!/usr/bin/python3
"""
Create class Square, child class of Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creates class Square

    Args:
        def __init__(self, size) - Constructor
    """
    def __init__(self, size):
        """
        Constructor
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        computes area
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        Print friendly format
        """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
