#!/usr/bin/python3
"""Defines a  Rectangle class that inherits from BaseGeometry."""
from typing import Union
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the rectangle using BaseGeometry."""

    def __init__(self, width: int, height: int):
        """Initialization of  new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of  new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self) -> int:
        """Returns the rectangle area ."""
        return (self.__width * self.__height)

    def __str__(self) -> str:
        """Returns  print() and str() representation of  Rectangle."""
        return (f"[{self.__class__.__name__}] {self.__width}/{self.__height}")
