#!/usr/bin/python3
"""
function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends a line of text after each line containing
    a specific string in a file.
    Args:
        filename (str): Name of the file
        search_string (str): Specific string to search for in each line
        new_string (str): Line of text to insert after the lines
        containing the search string
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Reset file pointer to the beginning

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()  # Remove any remaining content after writing
