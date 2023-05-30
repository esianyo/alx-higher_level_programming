#!/usr/bin/python3
# 5-square.py
# Esianyo Dzisenu <esianicd@gmail.com>

"""This class defines a square."""

class Square:
    """
    Private instance attribute: size

    Attribute:
        size (int): size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializes a square instance

        Args:
            size (int): The size of the square (default 0)
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of square

        Returns:
            int: an integer value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of square

        Args:
            value (int): size of square
        Raises:
            TypeError: Prints error message if size is not integer
            ValueError: Prints error if the value of size is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #

        If size is equal to 0, prints an empty line
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
