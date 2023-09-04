#!/usr/bin/python3
"""Task number 8"""


class Rectangle:
    """Representation of  a rectangle.

    Attributes:
        number_of_instances (int): number of Rectangle instances.
        print_symbol (any):  symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize The new Rectangle.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the Rectangle."""
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
        """Get height of the Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retuns the area of  Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns  perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns  Rectangle with the greater area.

        Args:
            rect_1 (Recto): first Rectangle.
            rect_2 (Recto): second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Return  printable representation of the Rectangle.

        Represents rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recto = []
        for x in range(self.__height):
            [recto.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                recto.append("\n")
        return ("".join(recto))

    def __repr__(self):
        """Returns  string representation of the Rectangle."""
        recto = "Rectangle(" + str(self.__width)
        recto += ", " + str(self.__height) + ")"
        return (recto)

    def __del__(self):
        """Print message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
