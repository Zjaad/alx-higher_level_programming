#!/usr/bin/python3
"""Defines a checking class func."""


def is_same_class(obj, a_class):
    """Check if the object is  an instance of a given class.

    Args:
        obj (any): obj to check.
        a_class (type): class to mmatch the type of objc to.
    Returns:
        True if the obj is exactly an instance of a_class , otherwhise False.
    """
    if type(obj) == a_class:
        return (True)
    return (False)
