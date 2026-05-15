#!/usr/bin/env python3
"""
Module demonstrating mixins with a Dragon class that can swim and fly.
"""


class SwimMixin:
    """
    Mixin providing swimming behavior.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin providing flying behavior.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class combining swimming and flying abilities via mixins.
    """

    def roar(self):
        """
        Print dragon roar behavior.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
