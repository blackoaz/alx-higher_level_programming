#!/usr/bin/python3
""""module for adding arguments to a python list"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
try:
    my_file = load_from_json_file(filename)
except FileNotFoundError:
    my_file = []
my_file.extend(sys.argv[1:])
save_to_json_file(my_file, filename)
