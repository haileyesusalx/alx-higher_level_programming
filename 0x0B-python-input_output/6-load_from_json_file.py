#!/usr/bin/python3
"""define"""
import json


def load_from_json_file(filename):
    """Returnthe Json"""
    with open(filename)as f:
    return json.load(f)
