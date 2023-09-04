#!/usr/bin/python3
""" task 7 Change representation"""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the new Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the Rectangle."""
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
        """set the height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return  area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return  perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        
        if self.__width == 0 or self.__height == 0:
            return ("")

        recto = []
        for x in range(self.__height):
            [recto.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                recto.append("\n")
        return ("".join(recto))

    def __repr__(self):
        """representation of the Rectangle."""
        recto = "Rectangle(" + str(self.__width)
        recto += ", " + str(self.__height) + ")"
        return (recto)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
