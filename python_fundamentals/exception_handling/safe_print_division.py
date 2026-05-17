#!/usr/bin/env python3
"""Module that divides two integers safely."""


def safe_print_division(a, b):
    """Divide two integers and print the result."""
    result = None
    try:
        result = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
