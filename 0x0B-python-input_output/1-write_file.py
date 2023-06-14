#!/usr/bin/python3
"""Writes a file."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)

    Args:
        filename: The path to the text file.
    text: The string to write to the file.

    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
