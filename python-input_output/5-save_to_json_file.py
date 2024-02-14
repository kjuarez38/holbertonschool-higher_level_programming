#!/usr/bin/python3
"""save to json file"""


def save_to_json_file(my_obj, filename):
    """save to json file"""
    import json
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
