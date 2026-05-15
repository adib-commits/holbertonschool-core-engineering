#!/usr/bin/env python3
"""
Module that defines an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Returns the sound made by the animal.
        Must be implemented by subclasses.
        """
        pass


class Dog(Animal):
    """
    Represents a Dog, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Represents a Cat, subclass of Animal.
    """

    def sound(self):
        """
        Returns the sound of a cat.
        """
        return "Meow"
