#!/usr/bin/python3
"""
file : 4-square.py
"""
class Square:
    """
    Representation of the square
    """
    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Return the current area of square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of  square.

        Args:
            value (int): The new size of  the square.

        Raises:
            TypeError: If value is not  integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
