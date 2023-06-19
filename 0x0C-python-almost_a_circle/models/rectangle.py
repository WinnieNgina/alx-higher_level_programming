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
        if (type(value) != int):
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
        if (type(value) != int):
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
        if (type(value) != int):
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
        if (type(value) != int):
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
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width), end="")
            print()

    def __str__(self):
        """
        String represantation
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        update instance attributes
        """
        if (len(args) > 0):
            try:

                self.id = args[0]
            except IndexError:
                pass

            try:

                self.width = args[1]
            except IndexError:
                pass

            try:

                self.height = args[2]
            except IndexError:
                pass

            try:

                self.x = args[3]
            except IndexError:
                pass

            try:

                self.y = args[4]
            except IndexError:
                pass

        else:
            args_list = ["id", "width", "height", "x", "y"]

            for attrs in args_list:
                if attrs in kwargs:
                    if attrs == "width":
                        self.width = kwargs[attrs]
                    if attrs == "height":
                        self.height = kwargs[attrs]
                    if attrs == "x":
                        self.x = kwargs[attrs]
                    if attrs == "y":
                        self.y = kwargs[attrs]
                    if attrs == "id":
                        self.id = kwargs[attrs]
                else:
                    pass

    def to_dictionary(self):
        """
        Return dictionary representation
        """
        my_dict = {}

        my_dict['id'] = self.id
        my_dict['width'] = self.width
        my_dict['height'] = self.height
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
