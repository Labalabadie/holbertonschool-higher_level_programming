#!/usr/bin/python3
"""New Class module"""


class Square:
    """New Square class"""

    def __init__(self, size=0):
        """New instance of a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout, sqauare of '#'"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()

    @property
    def size(self):
        """Gets size"""
        return (self.__size)

    @size.setter
    def size(self, size):
        """Sets size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
