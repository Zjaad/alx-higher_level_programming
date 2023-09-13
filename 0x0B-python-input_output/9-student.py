#!/usr/bin/python3
"""Class that defines a student."""


class Student:
    """Representation of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of a new Student.

        Args:
            first_name (str): First name.
            last_name (str): Last name.
            age (int): Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A dictionary representation of the student."""
        return (self.__dict__)
