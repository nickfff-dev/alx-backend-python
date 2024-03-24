#!/usr/bin/env python3

"""
This module provides a function to calculate
the floor of a floating-point number.

The floor function takes one parameter, a float,
and returns its floor value as an integer.
This module is designed to be imported and used in other Python scripts.
"""

import math


def floor(n: float) -> int:
    """
    Calculates the floor of a floating-point number
    and returns the result as an integer.

    Parameters:
    n (float): The floating-point number to calculate the floor of.

    Returns:
    int: The floor of n.
    """
    return math.floor(n)
