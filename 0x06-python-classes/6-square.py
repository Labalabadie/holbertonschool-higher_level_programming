#!/usr/bin/python3
"""New Class module"""


class Square:
    """New Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """New instance of a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """Returns square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout, square of '#'"""
        for i in range(self.size):
            for k in range(self.__position[0]):
                if self.__position[1] <= 0:
                    print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
        if self.size == 0:
            print()

    @property
    def size(self):
        """Gets size"""
        return (self.__size)

    def position(self):
        """Gets position"""
        return (self.__position)

    @size.setter
    def size(self, size):
        """Sets size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def position(self, value):
        """Sets position value"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        for elem in value:
            if type(elem) is not int:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
