#!/usr/bin/python3

class Rectangle:
    """ rectangle def """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """ width """
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    """ height """
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (self.__width * 2 + self.__height * 2) if (self.__width > 0 and self.__height > 0) else 0

    def draw(self):
        res = ""
        for y in range(self.__height):
            for x in range(self.__width):
                res += "#"
            if y != self.__height - 1:
                res += "\n"
        return res

    def __str__(self):
        return self.draw()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
