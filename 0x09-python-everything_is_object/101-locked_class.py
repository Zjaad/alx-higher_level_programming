#!/usr/bin/python3

class LockedClass:
    """
    Prevents users from dynamically creating new instance attributes,
    except if new instance attribute is called first_name.

    Attributes:
        first_name (str): first name.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Initializes a new instance of LockedClass."""
        self.first_name = None
