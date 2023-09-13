#!/usr/bin/python3
"""Function that writes a string to a text file UTF8 and returns the number of characters written."""


def write_file(filename="", text=""):
    """The function that write string to UTF8 text.

    Args:
        filename (str): The file to write.
        text (str): To write to the file.
    Returns:
        The number of characters.
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return (fl.write(text))
