#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        if a % 2 != 0:
            a = int(a)
    except TypeError:
        raise TypeError("a must be an integer")
    try:
        if b % 2 != 0:
            b = int(b)
    except TypeError:
        raise TypeError("b must be an integer")
    return (a + b)
