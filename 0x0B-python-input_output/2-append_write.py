#!/usr/bin/python3
"""Appends to a file"""


def append_write(filename="", text=""):
    """Function that appends to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
