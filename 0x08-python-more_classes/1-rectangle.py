#!/usr/bin/python3

"""
Rectangle class

Defines a rectangle with a width and height.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

Methods:
    __init__(width, height): Initializes the rectangle with the specified width and height.
    area(): Returns the area of the rectangle.
    perimeter(): Returns the perimeter of the rectangle.
    diagonal(): Returns the diagonal of the rectangle.
"""

class Rectangle:

    """Defines the rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with the specified width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("heght must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.height = height
        self.width = width
