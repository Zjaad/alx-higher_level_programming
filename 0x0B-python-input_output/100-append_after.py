#!/usr/bin/python3
"""A function that defines text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line contain the given str in file.

    Args:
        filename (str): The file name.
        search_string (str): Str to search for in file.
        new_string (str): Insert str.
    """
    txt = ""
    with open(filename) as k:
        for li in k:
            txt += li
            if search_string in li:
                txt += new_string
    with open(filename, "w") as p:
        p.write(txt)
