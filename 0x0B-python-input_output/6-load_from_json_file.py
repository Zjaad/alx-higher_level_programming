#!/usr/bin/python3
"""Function that creates an Object from a JSON."""
import json


def load_from_json_file(filename):
    """Create a Py obj from a JSON."""
    with open(filename) as fl:
        return (json.load(fl))
