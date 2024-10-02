#!/usr/bin/python3

"""
a basic serialization module that adds the functionality
to serialize a Python dictionary to a JSON file and
deserialize the JSON file to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file_json:
        json.dump(data, file_json)


def load_and_deserialize(filename):
    with open(filename, "r") as file_json:
        data = json.load(file_json)

    return (data)
