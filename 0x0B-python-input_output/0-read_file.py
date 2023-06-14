#!/usr/bin/python3
"""Reads files."""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
