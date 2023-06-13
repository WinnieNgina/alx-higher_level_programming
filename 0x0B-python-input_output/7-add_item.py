#!/usr/bin/python3
"""
add arguments to Python list
"""
import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item():

    """
    add arguments to python list
    and save to file
    """
    try:
        item_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        item_list = []

    for args in sys.argv[1:]:
        item_list.append(args)

    save_to_json_file(item_list, "add_item.json")


add_item()
