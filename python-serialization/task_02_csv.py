#!/usr/bin/python3

"""
function named convert_csv_to_json that takes the
CSV filename as its parameter and writes the JSON
data to data.json
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    opens a csv file and reads the data
    """
    with open(filename) as csv_file:
        data = csv.DictReader(csv_file)

    with open("data.json", "w") as json_file:
        json_file.write(json.dumps(data))
