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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Gets width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        # print(f"\tChecking width {value}")
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Gets height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        # print(f"\tChecking height {value}")
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        Gets x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        # print(f"\tChecking x {value}")
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        Gets y value
        """
        return self.__y

    @y.setter
    def y(self, value):
        # print(f"\tChecking y {value}")
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        Calculate area of the rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """
        Prints a rectangle shape
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()
