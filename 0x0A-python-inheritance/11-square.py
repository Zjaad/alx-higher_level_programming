#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
from typing import Union

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width: int, height: int):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.width * self.height

    def __str__(self) -> str:
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.width}/{self.height}"

    def integer_validator(self, name: str, value: int):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size: int):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
