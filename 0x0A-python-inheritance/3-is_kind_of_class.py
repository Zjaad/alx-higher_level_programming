#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against.

    Returns:
        True if obj is an instance of, or inherited from, a_class; otherwise, False.
    """
    return isinstance(obj, a_class)
