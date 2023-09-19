#!/usr/bin/python3
"""Defination of the class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Representation of rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identity of the  Rectangle.
        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height <= 0.
            TypeError: If either x or y isnt an integer.
            ValueError: If either  x or y < 0.
        """
        self.width = width
        self.height = height
        self.x_coordinate = x
        self.y_coordinate = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x_coordinate(self):
        """Get the x coordinate of Rectangle."""
        return (self.__x_coordinate)

    @x_coordinate.setter
    def x_coordinate(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x_coordinate = value

    @property
    def y_coordinate(self):
        """Get the y coordinate of Rectangle."""
        return self.__y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y_coordinate = value

    def area(self):
        """Returns the area of Rectangle."""
        return (self.width * self.height)

    def display(self):
        """Prints Rectangle using the `#`."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y_coordinate)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x_coordinate)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id
                - 2nd argument represents width
                - 3rd argument represent height
                - 4th argument represents x coordinate
                - 5th argument represents y coordinate
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            d = 0
            for arg in args:
                if d == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x_coordinate, self.y_coordinate)
                    else:
                        self.id = arg
                elif d == 1:
                    self.width = arg
                elif d == 2:
                    self.height = arg
                elif d == 3:
                    self.x_coordinate = arg
                elif d == 4:
                    self.y_coordinate = arg
                d += 1

        elif kwargs and len(kwargs) != 0:
            for t, v in kwargs.items():
                if t == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x_coordinate, self.y_coordinate)
                    else:
                        self.id = v
                elif t == "width":
                    self.width = v
                elif t == "height":
                    self.height = v
                elif t == "x":
                    self.x_coordinate = v
                elif t == "y":
                    self.y_coordinate = v

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x_coordinate,
            "y": self.y_coordinate
        }

    def __str__(self):
        """Returns print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x_coordinate, self.y_coordinate,
                                                       self.width, self.height)
