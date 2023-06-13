#!/usr/bin/python3

"""
Jsonify string
"""
import json


def to_json_string(my_obj):
    """
    returns JSON rep of an object(string)
    """
    return json.dumps(my_obj)
