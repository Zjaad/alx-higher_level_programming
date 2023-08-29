#!/usr/bin/python3

"""
Module Documentation: 1-square

This module created to define the Square class.
"""

class Square:
    """
    Square class with private instance attribute the size
    """
    def __init__(self, size):
        """
        Intializing the Square instance.

        args:
            size (int): The Size of the Square.

        Attributes:
            __size (int): The private instance that represent the size.
        """
        self.__size = size
