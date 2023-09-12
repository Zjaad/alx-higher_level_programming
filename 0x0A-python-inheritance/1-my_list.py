#!/usr/bin/python3
""" Task numtwo"""

class MyList(list):
    """Enables sorted printing for instances of the built-in list class."""
    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
