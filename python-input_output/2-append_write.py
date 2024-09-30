#!/usr/bin/python3

"""
a function that appends a string at the end of a text file and
returns the number of chars added
"""


def append_write(filename="", text=""):
    """
    Args:
        filename (str, optional): the name of the file to write
        text (str, optional): the string to write in the file

    Returns:
        int: the number of chars written to the file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
