#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0 or n >= len(string):
        return string  # Return the original string if n is out of bounds

    new_string = ""  # Initialize an empty string to store the modified string

    for i in range(len(string)):
        if i != n:
            new_string += string[i]
            # Append the character to the new string if it's not at position n

    return new_string
