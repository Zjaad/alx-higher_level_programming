#!/usr/bin/python3
"""task number 3"""


class Rectangle:
    """Representation of the rectangle."""

    def __init__(self, we=0, h=0):
        """Initialization of the new Rectangle.

        Args:
            we (int):  width of the new rectangle.
            h (int):  height of the new rectangle.
        """
        self.we = we
        self.h = h

    @property
    def we(self):
        """Get the width of the Rectangle."""
        return (self.__width)

    @we.setter
    def we(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def h(self):
        """Get height of the Rectangle."""
        return (self.__height)

    @h.setter
    def h(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns  area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns  perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a printable representation of the Rectangle.

        Representation of rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recto = []
        for x in range(self.__height):
            [recto.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                recto.append("\n")
        return ("".join(recto))
