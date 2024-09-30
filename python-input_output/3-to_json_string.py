#!/usr/bin/python3

"""
function that returns the JSON representation of an object
"""

import json


def to_json_string(my_obj):
    """

    Args:
        my_obj (_type_): object to be return as a JSON repr

    Returns:
        string: returning object as string
    """
    my_string = json.dumps(my_obj)
    return (my_string)
