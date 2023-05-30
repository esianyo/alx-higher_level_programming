#!/usr/bin/python3
# -square.py
# Esianyo Dzisenu <esianicd@gmail.com>
"""This class defines a square."""

class Square:
    """
    Private instance attribute: size

    Arttribute:
        size (int): size of the square (private)
    """

    def __init__(self, size):
        """
        Square instance initialisation

        Args:
            size (int): this is size of the square
        """
        self.__size = size
