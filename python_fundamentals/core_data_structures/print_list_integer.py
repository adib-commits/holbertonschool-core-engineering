#!/usr/bin/env python3
"""Print list of integers"""


def print_list_integer(my_list=[]):
    """Print all integers in a list"""
    for number in my_list:
        print("{:d}".format(number))
