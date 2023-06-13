#!/usr/bin/python3

"""
write a json string to a .txt file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write a json string to a text file
    """
    with open(filename, 'w', encoding="utf-8") as text_file:
        text_file.write(json.dumps(my_obj))
