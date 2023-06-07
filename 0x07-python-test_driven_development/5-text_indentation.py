#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print(char)
            print()
            skip_space = True
        elif char == ' ' and skip_space:
            continue
        else:
            print(char, end='')
            skip_space = False
