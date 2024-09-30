#!/usr/bin/python3

"""
function that writes a string to a text file a
returns the number of chars written
"""


def write_file(filename="", text=""):
    """_summary_

    Args:
        filename (str, optional): the name of the file to write to
        text (str, optional): the string to write in the file

    Returns:
        int: the number of chars written to the file
    """

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
