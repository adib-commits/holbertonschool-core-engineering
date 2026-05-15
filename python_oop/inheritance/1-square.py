#!/usr/bin/env python3
"""
Module that defines the Square class
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a square with a given size
        """
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)
