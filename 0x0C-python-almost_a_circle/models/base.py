#!/usr/bin/python3
"""
Creates class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert dictionary to JSON repr
        """
        if (len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json string to file
        """

        dict_list = []

        # Loop through list_objs  invoke it's
        # .to_dictionary method to convert it to a dict

        for inst in list_objs:
            dict_list.append(inst.to_dictionary())

        # Append each dictionary into a list

        # Convert the list to json string using
        # the static method to_json_string()

        json_dict_list = cls.to_json_string(dict_list)

        # Save the json string repr of the list of dictionaries into file

        file_name = cls.__name__ + ".json"
        with open(file_name, 'w', encoding="utf-8") as json_file:
            json_file.write(json_dict_list)
