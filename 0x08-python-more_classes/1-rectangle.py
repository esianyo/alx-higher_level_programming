#!/usr/bin/python3


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        Initialising

        Args:
           width (int, optional): the width of the rectangle
           height (int, optional): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Width setter

        Args:
           width (int, optional): the width of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is not >= 0
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Height setter

        Args:
           height (int, optional): the height of the rectangle

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is not >= 0
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
