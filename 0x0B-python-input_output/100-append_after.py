#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
