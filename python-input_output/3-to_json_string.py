#!/usr/bin/python3
import json

"""
function that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """_summary_

    Args:
        my_obj (_type_): object to be return as a JSON repr

    Returns:
        string: returning object as string
    """
    my_string = json.dumps(my_obj)
    return (my_string)
