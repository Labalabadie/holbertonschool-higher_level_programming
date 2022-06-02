#!/bin/usr/python3
"""Hola"""
from models.base import Base


class Rectangle(Base):
    """Hola"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Holi"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width getter"""
        return (self.__width)
    @width.setter
    def width(self, width):
        """Width setter"""
        self.__width = width

    @property
    def height(elf):
        """height getter"""
        return (self.__height)
    @height.setter
    def height(self, height):
        """height setter"""
        self.__height = height
            
    @property
    def x(self):
        """x getter"""
        return (self.__x)
    @width.setter
    def x(self, x):
        """x setter"""
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return (self.__y)
    @y.setter
    def y(self, y):
        """y setter"""
        self.__y = y
