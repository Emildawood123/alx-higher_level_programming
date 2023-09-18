#!/usr/bin/python3
"""class module base"""
import json
from turtle import *


class Base:
    """cls"""
    __nb_objects = 0

    """defs"""
    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """funcation"""
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """def"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """cls method"""
        instance = None
        if cls.__name__ != "Rectangle":
            instance = cls(1)
        else:
            instance = cls(1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def save_to_file(cls, list_objs):
        """def"""
        name = cls.__name__
        my_list = []
        for n in list_objs:
            my_list.append(cls.to_dictionary(n))
        with open("{}.json".format(name), "w", encoding="utf-8") as file:
            file.write(cls.to_json_string(my_list))

    @classmethod
    def load_from_file(cls):
        """def"""
        name = cls.__name__
        try:
            with open("{}.json".format(name), "r", encoding="utf-8") as file:
                to_obj = cls.from_json_string(file.read())
                my_list = []
                for i in to_obj:
                    my_list.append(cls.create(**i))
                return (my_list)
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """def"""
        arrow = Turtle()
        arrow.speed(1)
        for rect in list_rectangles:
            arrow.color("black", "blue")
            arrow.begin_fill()
            arrow.penup()
            arrow.forward(rect.x)
            arrow.right(90)
            arrow.forward(rect.y)
            arrow.pendown()
            arrow.left(90)
            arrow.forward(rect.width)
            arrow.right(90)
            arrow.forward(rect.height)
            arrow.right(90)
            arrow.forward(rect.width)
            arrow.right(90)
            arrow.forward(rect.height)
            arrow.penup()
            arrow.setx(0)
            arrow.sety(0)
            arrow.right(90)
            arrow.pendown()
            arrow.end_fill()
        for squ in list_squares:
            arrow.color("black", "red")
            arrow.begin_fill()
            arrow.penup()
            arrow.forward(squ.x)
            arrow.right(90)
            arrow.forward(squ.y)
            arrow.pendown()
            arrow.left(90)
            for i in range(0, 3):
                arrow.forward(squ.size)
                arrow.right(90)
            arrow.forward(squ.size)
            arrow.penup()
            arrow.setx(0)
            arrow.sety(0)
            arrow.right(90)
            arrow.pendown()
            arrow.end_fill()
        done()
