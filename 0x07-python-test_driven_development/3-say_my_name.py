#!/usr/bin/python3
"""
Prints name
Esianyo Dzisenu
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Alice")
        My name is Alice
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name
    if last_name:
        full_name += " " + last_name

    print("My name is", full_name)
