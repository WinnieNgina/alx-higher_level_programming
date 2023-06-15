#!/usr/bin/python3

"""
Create class Rectangle
"""

from .base import Base


class Rectangle(Base):
    """
    Class Rectangle

    Args:
        def __init__(self, width, height, x=0, y=0, id=None)
        @property
        def width(self)
        @width.setter
        def set_width(self, value)
        @property
        def height(self)
        @height.setter
        def set_height(self, value)
        @property
        def x(self)
        @x.setter
        def set_x(self, value)
        @property
        def y(self)
        @y.setter
        def set_y(self, value)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets width value
        """
        return self.__width

    @width.setter
    def set_width(self, value):
        self.__width = value

    @property
    def height(self):
        """
        Gets height value
        """
        return self.__height

    @height.setter
    def set_height(self, value):
        self.__height = value

    @property
    def x(self):
        """
        Gets x value
        """
        return self.__x

    @x.setter
    def set_x(self, value):
        self.__x = value

    @property
    def y(self):
        """
        Gets y value
        """
        return self.__y

    @y.setter
    def set_y(self, value):
        self.__y = value
