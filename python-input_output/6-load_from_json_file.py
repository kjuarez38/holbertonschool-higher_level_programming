#!/usr/bin/python3
"""load from json file"""


def load_from_json_file(filename):
    """load from json file"""
    import json
    with open(filename, 'r') as file:
        return json.loads(file.read())
