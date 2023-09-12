#!/usr/bin/python3
"""Defines the subclass Rectangle  Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of  square."""

    def __init__(self, size):
        """Initialization of the new square.

        Args:
            size (int): Size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
