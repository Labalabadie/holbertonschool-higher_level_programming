#!/usr/bin/python3
"""Module that writes a string to a text file"""
def write_file(filename="", text=""):
    """Opens file in writing mode"""
    with open(filename, mode='w', encoding='utf-8') as b_file:
        return (b_file.write(text))
