#!/usr/bin/python3
"""Class Student that defines a student."""


class Student:
    """Representation of a student."""

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
        """Dictionary that represente the Student.

        If attrs is list of str, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {p: getattr(self, p) for p in attrs if hasattr(self, p)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replace attributes of the Student.

        Args:
            json (dict): The value pairs to replace attributes with.
        """
        for p, y in json.items():
            setattr(self, p, y)
