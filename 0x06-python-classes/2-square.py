#!/usr/bin/python3
"""New module about classes"""


class Square:
    """Class, square with size"""

    def __init__(self, size=0):
        """New square instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
