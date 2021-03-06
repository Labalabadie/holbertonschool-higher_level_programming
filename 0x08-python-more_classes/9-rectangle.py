#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes instance"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a str representation of a rectangle instance with '#'"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            return (f"{str(self.print_symbol)*self.width}\n"
                    * self.height).strip('\n')

    def __repr__(self):
        """Representation of a rectangle"""
        return (f"{self.__class__.__name__}({self.width}, {self.height})")

    def __del__(self):
        """Delete an instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """returns area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter"""
        return self.__width*2 + self.__height*2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle width == height"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
