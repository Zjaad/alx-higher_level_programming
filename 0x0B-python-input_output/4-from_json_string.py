#!/usr/bin/python3
"""JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return Py object representation of JSON str."""
    return (json.loads(my_str))
