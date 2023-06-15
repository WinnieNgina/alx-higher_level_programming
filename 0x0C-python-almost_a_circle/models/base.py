#!/usr/bin/python3
"""
Creates class Base
"""


class Base:
    """
    class Base
    args:
    def __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
