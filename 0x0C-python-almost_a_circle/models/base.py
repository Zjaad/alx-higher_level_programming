#!/usr/bin/python3
"""
This module defines the Base class.
"""

import json
import csv
import turtle

class Base:
    """
    The Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a new instance of a Base class.

        Args:
            id (int, optional): The id of a new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_of_dicts):
        """Returns JSON serialization of dictionaries list."""
        if not list_of_dicts:
            return ("[]")
        return (json.dumps(list_of_dicts))

    @classmethod
    def save_to_file(cls, list_of_objs):
        """Writes  JSON serialization."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if not list_of_objs:
                jsonfile.write("[]")
            else:
                list_of_dicts = [obj.to_dictionary() for obj in list_of_objs]
                jsonfile.write(Base.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_str):
        """Return the deserialization of a JSON string."""
        if not json_str or json_str == "[]":
            return []
        return (json.loads(json_str))

    @classmethod
    def create(cls, **attrs):
        """Returns class instantiated from a dic of attr."""
        if attrs and attrs != {}:
            new_instance = cls(1 if cls.__name__ == "Rectangle" else 1)
            new_instance.update(**attrs)
            return (new_instance)

    @classmethod
    def load_from_file(cls):
        """Returns list of classes instantiated from file of JSON str."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_of_dicts = Base.from_json_string(jsonfile.read())
                return ([cls.create(**d) for d in list_of_dicts])
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_of_objs):
        """Writes a CSV serialization of list of objs to file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if not list_of_objs:
                csvfile.write("[]")
            else:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_of_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns  list of classes instantiated from the CSV."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = (
                    ["id", "width", "height", "x", "y"]
                    if cls.__name__ == "Rectangle"
                    else ["id", "size", "x", "y"]
                )
                list_of_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_of_dicts = [dict([k, int(v)] for k, v in d.items()) for d in list_of_dicts]
                return [cls.create(**d) for d in list_of_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(rectangles, squares):
        """Draw Squares and triangles using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        def draw_shape(shape, color, attrs):
            turt.showturtle()
            turt.up()
            turt.goto(attrs["x"], attrs["y"])
            turt.down()
            for _ in range(2):
                turt.forward(attrs["width"])
                turt.left(90)
                turt.forward(attrs["height"])
                turt.left(90)
            turt.hideturtle()

        turt.color("#ffffff")
        for rect in rectangles:
            draw_shape(rect, "#ffffff", rect.to_dictionary())

        turt.color("#b5e3d8")
        for sq in squares:
            draw_shape(sq, "#b5e3d8", sq.to_dictionary())

        turtle.exitonclick()
