#!/usr/bin/python3
"""Module that works with JSON and object"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an objet to a text file using a JSON representation"""
    with open(filename, mode='w') as d_file:
        json_my_obj = json.dumps(my_obj)
        d_file.write(json_my_obj)
