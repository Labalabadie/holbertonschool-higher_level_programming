#!/usr/bin/python3
"""Module that creates object from a JSON file"""

import json


def load_from_json_file(filename):
    """Creates Objet from a "JSON" file"""
    with open(filename) as e_file:
        return (json.loads(e_file.read()))
