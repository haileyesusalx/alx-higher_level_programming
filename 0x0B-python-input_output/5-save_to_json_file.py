#!/usr/bin/python3
"""define"""
import json


def save_to_json_string(my_obj, filename):
    """Returnthe Json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
