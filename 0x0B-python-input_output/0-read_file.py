#!/usr/bin/python3
"""Function that reads a text UTF8 and prints it."""
def read_file(filename=""):
    """Function read_file.""" 
    with open(filename, encoding='utf-8') as fi:
        print(fi.read(), end= "")       
