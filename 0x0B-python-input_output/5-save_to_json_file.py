#!/usr/bin/python3
"""A function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """An object to text using JSON representation."""
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
