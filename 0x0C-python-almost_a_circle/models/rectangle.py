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

    def type_int_validator(var, name):
        """Hola pie te quedaste aca, tenes que validar todos los casos ejercicio 3 sin escribir todo a mano, besitos bestios chau chau, """
        if type(var) is not int
            raise TypeError("{name} must be an interger",)
        if width <= 0:
            raise ValueError("width must be > 0")
        
    @property
    def width(self):
        """Width getter"""
        return (self.__width)
    @width.setter
    def width(self, width):
        """Width setter"""
        if type(width) is not int:
            raise TypeError("width must be an interger")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter"""
        return (self.__height)
    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) != type(int):
            raise TypeError("height must be an interger")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
            
    @property
    def x(self):
        """x getter"""
        return (self.__x)
    @width.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an interger")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return (self.__y)
    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an interger")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
