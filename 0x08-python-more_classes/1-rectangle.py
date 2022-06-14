#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializes instance"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @property
    def height(self):
        """Height setter"""
        return self.__height

    @width.setter
    def width(self, value):
        """Width getter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Height getter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
