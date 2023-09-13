#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """Appends string to the end of a UTF8 text.

    Args:
        filename (str): The file to append to.
        text (str): string to append to file.
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
