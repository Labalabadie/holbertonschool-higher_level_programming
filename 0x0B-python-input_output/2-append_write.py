#!/usr/bin/python3
"""Module which opens a files in append mode"""


def append_write(filename="", text=""):
    """opens file, and returns number of characters appended"""
    with open(filename, mode='a', encoding='utf-8') as c_file:
        return (c_file.write(text))
