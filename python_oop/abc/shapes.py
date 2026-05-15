#!/usr/bin/env python3
"""
Module that defines an abstract Shape class and concrete Circle and Rectangle classes.
Also includes a duck-typed function shape_info.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """

    @abstractmethod
    def area(self):
        """
        Returns the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Returns the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle shape.
    """

    def __init__(self, radius):
        """
        Initialize a circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Compute and return the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Compute and return the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing.

    The function does not check the type of the object,
    it only assumes it has area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
