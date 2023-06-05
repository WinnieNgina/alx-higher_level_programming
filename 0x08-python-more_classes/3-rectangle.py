#!/usr/bin/python3
""" Create class: Rectangle """


class Rectangle:
    """Empty class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle.

        Args:
            __width(int): Width of rectangle
            __height(int): Height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ Getter for height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ Getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """Calculates area of a rectangle"""
        return (self.height * self.width)

    def perimeter(self):
        """Calculates perimeter of a rectangle"""
        if (self.height == 0 or self.width == 0):
            return (0)
        else:
            return ((self.height + self.width) * 2)

    def __str__(self):
        """Prints rectangle using # shapes"""
        my_list = ""
        if (self.width == 0 or self.height == 0):
            return ("")
        else:
            for j in range(self.height):
                for i in range(self.width):
                    my_list += "#"
                if (j < self.height - 1):
                    my_list += "\n"
            return (my_list)
