#!/usr/bin/env python3
"""
Module that defines VerboseList, a subclass of list
that prints messages on modifications.
"""


class VerboseList(list):
    """
    A list that prints notifications when modified.
    """

    def append(self, item):
        """
        Add an item to the list and print a message.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list and print number of added items.
        """
        length_before = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{length_before}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a message.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list and print a message.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
