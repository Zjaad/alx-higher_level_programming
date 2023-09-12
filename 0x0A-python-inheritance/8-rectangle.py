#!/usr/bin/python3
"""Defines a  Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intializes  new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
