#!/usr/bin/python3
"""From class to JSON"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""

    properties = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("__"):
            if isinstance(value, list):
                properties[key] = [class_to_json(item) for item in value]
            elif isinstance(value, dict):
                properties[key] = {k: class_to_json(v) for k, v in value.items()}
            elif isinstance(value, str):
                properties[key] = value
            elif isinstance(value, int):
                properties[key] = value
            elif isinstance(value, bool):
                properties[key] = value

    return properties
