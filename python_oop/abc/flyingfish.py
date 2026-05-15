#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    Represents a Fish.
    """

    def swim(self):
        """
        Print swimming behavior of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a Bird.
    """

    def fly(self):
        """
        Print flying behavior of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a Flying Fish using multiple inheritance.
    """

    def fly(self):
        """
        Override fly method for FlyingFish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override swim method for FlyingFish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override habitat method for FlyingFish.
        """
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    print(FlyingFish.mro())
