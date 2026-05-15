#!/usr/bin/env python3
"""
Module that defines a Square class.
"""


class Square:
    """
    Represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square.

        Args:
            size (int): Size of the square.
            position (tuple): Position of the square.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): New size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): New position.

        Raises:
            TypeError: If position is invalid.
        """

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """
        Return the current square area.

        Returns:
            int: Area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the # character.
        """

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))

    def __str__(self):
        """
        Return the string representation of the square.
        """

        if self.__size == 0:
            return ""

        square_lines = []

        for i in range(self.__position[1]):
            square_lines.append("")

        for i in range(self.__size):
            line = (" " * self.__position[0]) + ("#" * self.__size)
            square_lines.append(line)

        return "\n".join(square_lines)
