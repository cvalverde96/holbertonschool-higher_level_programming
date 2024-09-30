#!/usr/bin/python3

"""
function that returns an object (Python data structure)
represented by a JSON string
"""

import json


def from_json_string(my_str):
    """_summary_

    Args:
        my_str (_type_): json string

    Returns:
        obj: returns a python data structure
    """
    my_string = json.loads(my_str)
    return (my_string)
