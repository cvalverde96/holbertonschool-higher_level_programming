#!/usr/bin/python3

"""
function named convert_csv_to_json that takes the
CSV filename as its parameter and writes the JSON
data to data.json
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    opens a csv file and reads the data
    """
    try:
        with open(csv_filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            csv_data = [row for row in csv_reader]

        with open("data.json", "w") as json_file:
            json.dump(csv_data, json_file)
        return (True)

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return (False)

    except Exception as e:
        print(f"An error occurred: {e}")
        return (False)
