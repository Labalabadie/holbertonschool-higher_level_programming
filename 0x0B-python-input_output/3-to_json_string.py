#!/usr/bin/python3
"""Module that cast a string from an object with JSON"""

import json


def to_json_string(my_obj):
    """cast an object as a string and returns it"""
    return json.dumps(my_obj)
