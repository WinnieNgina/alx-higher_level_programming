#!/usr/bin/python3
"""
create class Student
"""


class Student:
    """
    Creates class Student

    args:
        def __init__ - constructor
        def to_json
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dict repr of instance
        """
        if attrs is None:
            return vars(self)
        else:
            attribute_dict = {}
            for attribute in attrs:
                if hasattr(self, attribute):
                    attribute_dict[attribute] = getattr(self, attribute)
            return attribute_dict

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
