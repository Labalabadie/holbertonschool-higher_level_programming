#!/usr/bin/python3
"""Module that creates a class student """


class Student:
    """Class Student"""


    def __init__(self, first_name, last_name, age):
        """ New instance"""
        self.first_name = first_name
        self.last_nmae = last_name
        self.age = age


    def to_json(self):
        """Returns a JSON of the class"""
        return self.__dict__
