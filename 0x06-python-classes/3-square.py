#!/usr/bin/python3
"""New Class Module"""


class Square:
    """New Square class"""

    def __init__(self, size=0):
        """New Instance of Square"""
        if type(size) is not int:
            raise TypeError("size must be and integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method, returns area of square"""
        return (self.__size * self.__size)
