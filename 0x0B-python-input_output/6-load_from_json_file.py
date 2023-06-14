#!/usr/bin/python3
"""Creates object from JSON file"""
import json


def load_from_json_file(filename):
    """The function"""
    with open(filename, "r", encoding="utf-8") as f:
        json_string = f.read()

    return json.loads(json_string)
