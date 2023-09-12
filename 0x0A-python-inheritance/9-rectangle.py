#!/usr/bin/python3
"""Defines the Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of new Rectangle.

        Args:
            width (int): width of  new Rectangle.
            height (int): height of  new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Returns print() and str() representation of a Rectangle."""
        strg = "[" + str(self.__class__.__name__) + "] "
        strg += str(self.__width) + "/" + str(self.__height)
        return (strg)
