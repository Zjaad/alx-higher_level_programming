#!/usr/bin/python3
"""Defines a Rectangle class. task 6: How many instances """


class Rectangle:
    """Represent the rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize hte new rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
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
        """Returns printable representation of the Rectangle.

        Represents  rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recto = []
        for x in range(self.__height):
            [recto.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                recto.append("\n")
        return ("".join(recto))

    def __repr__(self):
        """Return the string representation of rectangle."""
        recto = "Rectangle(" + str(self.__width)
        recto += ", " + str(self.__height) + ")"
        return (recto)

    def __del__(self):
        """Print  message for every deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
