#!/usr/bin/python3
def uppercase(str):
    ammended_string = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            ammended_char = chr(ord(c) - 32)
            ammended_string += ammended_char
        else:
            ammended_string += c
    print("{}".format(ammended_string))
