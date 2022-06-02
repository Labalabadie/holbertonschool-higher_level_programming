#!/usr/bin/python3
"""Class file"""


class Base():
    """New Class, nb_objects = amount """
    __nb_objects = 0

    def __init__(self, id=None):
        """Creates new instance and sets and ID"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
