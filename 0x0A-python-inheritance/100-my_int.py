#!/usr/bin/python3
"""Defines  MyInt class that inherits from int."""


class MyInt(int):
    """MyInt class"""
    def __eq__(self, value):
        """Override the != operator to compare real parts."""
        return (self.real != value)

    def __ne__(self, value):
        """Override the == operator to compare real parts."""
        return (self.real == value)
