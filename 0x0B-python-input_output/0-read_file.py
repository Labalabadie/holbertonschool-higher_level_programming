#!/usr/bin/python3
"""Module that read from a file, printing its content"""
def read_file(filename=""):
    """opens file"""
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            print(a_line, end="")
