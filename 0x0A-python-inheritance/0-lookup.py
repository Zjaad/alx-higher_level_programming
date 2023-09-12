#!/usr/bin/python3
"""Defines  object attribute lookup func."""


def lookup(obj):
    """Returns  list of the object is available attributes."""
    return dir(obj)
