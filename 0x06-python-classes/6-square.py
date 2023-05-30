#!/usr/bin/python3
# 6-square.py
# Esianyo Dzisenu <esianicd@gmail.com>

"""This class defines a square."""


class Square:
    """
    Private instance attribute: size

    Attribute:
        size (int): size of the square (private)
        position (tuple): position of the square (private)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square instance

        Args:
            size (int): The size of the square (default 0)
            position (tuple): The position of the square (default (0, 0))
        Raises:
            TypeError: If size is not an integer or position is not a tuple of 2 positive integers
            ValueError: If size is less than 0 or position values are less than 0
        """
        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

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
            TypeError: Prints error message if size is not an integer
            ValueError: Prints error if the value of size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square

        Returns:
            tuple: a tuple of 2 positive integers representing the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value (tuple): position of square
        Raises:
            TypeError: Prints error message if position is not a tuple of 2 positive integers
            ValueError: Prints error if position values are less than 0
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
