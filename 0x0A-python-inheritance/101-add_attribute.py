#!/usr/bin/python3
"""Defines the function that adds attributes to obj."""


def add_attribute(obj, att, value):
    """Add the new attribute to object.

    Args:
        obj (any): Obj to add an attribute to.
        att (str): The attribute name to add to obj.
        value (any): Att's value.
    Raises:
        TypeError: If impossible to add  the attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
