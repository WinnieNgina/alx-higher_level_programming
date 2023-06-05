#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if (i == '.' or i == '?' or i == ':'):
            print(i)
            print()
        else:
            print(i, end="")
