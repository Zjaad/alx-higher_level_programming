#!/usr/bin/python3
# 0-add_integer.py
""" addition function. """

def add_integer(a, b=98):
    """Returns integer addition of a and b.

    Float arguments are typecasted to int before addition is performed.

    Raises:
        TypeError: If  a or b is a non-integer , non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

