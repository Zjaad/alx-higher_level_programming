#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it """
def read_file(filename=""):
    """ function read_file """
    try:
        with open(filename, encoding='utf-8') as file:
            print(file.read(), end= "")
    except FileNotFoundError:
        pass
