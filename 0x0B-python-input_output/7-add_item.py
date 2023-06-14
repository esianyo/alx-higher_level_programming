#!/usr/bin/python3
"""Loads froma JSON file"""
import json
import sys


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file
    using a JSON representation.
    Args:
        my_obj: The object to serialize.
        filename: The path to the text file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f, indent=4)


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    Args:
        filename: The path to the JSON file.

    Returns:
        The object created from the JSON file.
    """

    with open(filename, "r", encoding="utf-8") as f:
        json_string = f.read()
    return json.loads(json_string)


if __name__ == "__main__":
    """Get all arguments passed to the script."""
    args = sys.argv[1:]
    items = []
    for arg in args:
        items.append(arg)
    save_to_json_file(items, "add_item.json")
    loaded_items = load_from_json_file("add_item.json")
    print(loaded_items)
