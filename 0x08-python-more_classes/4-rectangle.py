#!/usr/bin/python3
"""task number 4"""


class Rectangle:
    """Representation of the rectangle."""

    def __init__(self, we=0, h=0):
        """Initialization a new Rectangle.

        Args:
            we (int):  width of the new rectangle.
            h (int):  height of the new rectangle.
        """
        self.we = we
        self.h = h

    @property
    def we(self):
        """Get width of the Rectangle."""
        return (self.__we)

    @we.setter
    def we(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__we = value

    @property
    def h(self):
        """Get  height of the Rectangle."""
        return (self.__h)

    @h.setter
    def h(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__h = value

    def area(self):
        """Returns area of the Rectangle."""
        return (self.__we * self.__h)

    def perimeter(self):
        """Returns perimeter of the Rectangle."""
        if self.__we == 0 or self.__h == 0:
            return (0)
        return ((self.__we * 2) + (self.__h * 2))

    def __str__(self):
        """Returns a printable representation of the Rectangle.

        Representation of rectangle with the # character.
        """
        if self.__we == 0 or self.__h == 0:
            return ("")

        recto = []
        for x in range(self.__h):
            [recto.append('#') for y in range(self.__we)]
            if x != self.__h - 1:
                recto.append("\n")
        return ("".join(recto))

    def __repr__(self):
        """Returns  string representation of the Rectangle."""
        recto = "Rectangle(" + str(self.__we)
        recto += ", " + str(self.__h) + ")"
        return (recto)
