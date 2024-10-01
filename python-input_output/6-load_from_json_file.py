#!/usr/bin/python3

"""
function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):

    """
    Args:
        filename (str): The name of the file containing the JSON
    """
    with open(filename, 'r', encoding="utf-8") as file:
        my_obj = json.load(file)
        return (my_obj)
