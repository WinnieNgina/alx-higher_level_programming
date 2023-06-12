#!/usr/bin/python3
"""MyInt inherits from int"""


class MyInt(int):
    """
    MyInt has == and != operators inverted
    Returns False for integers(eq method)
    True an int != operator used
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
