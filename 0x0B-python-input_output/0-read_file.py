#!/usr/bin/python3
"""Function that reads a text UTF8 and prints it."""
def read_file(filename=""):
    """Function read_file.""" 
    with open(filename) as fi:
        rt = fi.read() 
        print(rt, end="")       
