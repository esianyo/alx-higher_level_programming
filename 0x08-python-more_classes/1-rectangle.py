#!/usr/bin/python3
"""
Rectangle class
Esianyo Dzisenu
"""


class Rectangle:

    """
    Rectangle class

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        __init__(width, height): Initialize the rectangle
        width: Get width of the rectangle.
        width: Set width of the rectangle.
        height: Get height of the rectangle.
        height: Set height of the rectangle.
        area: Get area of the rectangle.
    """

    # Private instance attributes

    __width = None
    __height = None

    # Property getter for width

    @property
    def width(self):
        return self.__width

    # Property setter for width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Property getter for height

    @property
    def height(self):
        return self.__height

    # Property setter for height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Instantiation with optional width and height

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # Get the area of the rectangle

    def area(self):
        return self.width * self.height
