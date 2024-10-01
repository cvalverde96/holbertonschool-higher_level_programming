#!/usr/bin/python3

"""
Function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """

    Args:
        obj: objecto to serialize

    Returns:
        __dict__: the dictionary discrption
    """
    return (obj.__dict__)
