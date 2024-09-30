#!/usr/bin/python3

"""
function that reads a text file and prints it to stdout
"""


def read_file(filename=""):

    """
    Args:
        filename (str, optional): the name of te file to read
    """

    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')