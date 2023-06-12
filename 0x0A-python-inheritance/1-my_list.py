#!/usr/bin/python3
"""
creat class MyList
"""


class MyList(list):
    """
    create class MyList
    """
    def print_sorted(self):
        """
        prints list sorted in ascending order
        """
        print(sorted(self))
