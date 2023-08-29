#!/usr/bin/python3
"""
a class Square that defines a square
"""

def ___init___(self, size=0):
    """
    initializing a new square
    
    args:
    size(int) : size of the square
    
    """
    if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
