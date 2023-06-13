#!/usr/bin/python3

"""
create an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    create an object from a JSON file
    """
    with open(filename, 'r', encoding="utf-8") as text_file:
        return json.loads(text_file.read())
