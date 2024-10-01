#!/usr/bin/python3

"""
a script that adds all arguments to a
Python list, and then save them to a file
"""
import sys
import os

save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

my_file = "add_item.json"

args = sys.argv[1:]

if os.path.exists(my_file):
    new_list = load_file(my_file)
else:
    new_list = []

new_list.extend(args)

save_file(new_list, my_file)
