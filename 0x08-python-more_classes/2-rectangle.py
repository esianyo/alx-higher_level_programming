#!/usr/bin/python3
"""
Rectangle class
Esianyo Dzisenu
"""


class Rectangle:

    """A class that represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
    """

    # Private instance attribute: width

    __width = None

    # Property def width(self): to retrieve it

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    # Property setter def width(self, value): to set it:

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Private instance attribute: height

    __height = None

    # Property def height(self): to retrieve it

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    # Property setter def height(self, value): to set it:

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Instantiation: def __init__(self, width=0, height=0):

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    # Public instance method: def area(self): that returns the rectangle area

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    # Public instance method: returns the rectangle perimeter:

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
