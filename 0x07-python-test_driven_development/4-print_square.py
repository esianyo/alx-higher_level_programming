#!/usr/bin/python3
"""
Prints square
Esianyo Dzisenu
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or if it is a float and less than 0.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####

        >>> print_square(2)
        ##
        ##

        >>> print_square(0)

        >>> print_square(-3)
        Traceback (most recent call last):
            ...
        ValueError: size must be >= 0

        >>> print_square(2.5)
        Traceback (most recent call last):
            ...
        TypeError: size must be an integer
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
