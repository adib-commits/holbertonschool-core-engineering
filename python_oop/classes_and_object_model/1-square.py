#!/usr/bin/env python3
"""
Module that defines a Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initialize a square with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
