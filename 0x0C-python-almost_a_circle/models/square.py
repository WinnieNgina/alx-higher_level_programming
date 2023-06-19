#!/usr/bin/python3

"""
Creates class Square
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
        args:
            def __init__(self, size, x = 0, y = 0, id=None):
            def __str__(self)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """
        Get size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update instance attributes
        """
        if (len(args) > 0):
            try:

                self.id = args[0]
                # print(f"\tUpdate id with args")
            except IndexError:
                pass

            try:

                self.size = args[1]
                # print(f"\tUpdate width with args")
            except IndexError:
                pass

            try:

                self.x = args[2]
                # print(f"\tUpdate x with args")
            except IndexError:
                pass

            try:

                self.y = args[3]
                # print(f"\tUpdate y with args")
            except IndexError:
                pass

        else:
            args_list = ["id", "size", "x", "y"]

            for attrs in args_list:
                if attrs in kwargs:
                    if attrs == "size":
                        self.size = kwargs[attrs]
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
        my_dict['size'] = self.width
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
