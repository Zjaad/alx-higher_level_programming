#!/usr/bin/python3
"""Class Student that defines a student based on 9-student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialization of the new Student.

        Args:
            first_name (str): First name.
            last_name (str): Last name.
            age (int): Age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representation of the Student.

        Represents attributes included in the list if the attrs is a list of str.

        Args:
            attrs (list): The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {p: getattr(self, p) for p in attrs if hasattr(self, p)}
        return (self.__dict__)
