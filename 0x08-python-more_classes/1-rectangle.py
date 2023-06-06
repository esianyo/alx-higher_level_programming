#!/usr/bin/python3
"""
Rectangle class
Esianyo Dzisenu
"""
class Rectangle:
    """Defines the rectangle"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("heght must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.height = height
        self. Width = width
