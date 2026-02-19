#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Add two numbers.

    Args:
        a: first number (int/float)
        b: second number (int/float), default 98

    Raises:
        TypeError: if a or b is not an int or float

    Returns:
        int: sum of a and b after casting floats to ints
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
