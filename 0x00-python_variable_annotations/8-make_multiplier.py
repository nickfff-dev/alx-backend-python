#!/usr/bin/env python3

"""
This module provides a function to create a multiplier function.

The make_multiplier function takes one parameter,
a float, and returns a function that multiplies
a float by the given multiplier.
This module is designed to be imported and used in other Python scripts.
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Creates a function that multiplies a float by the given multiplier.

    Parameters:
    multiplier (float): The multiplier to use for multiplication.

    Returns:
    typing.Callable[[float], float]: A function that takes a float and
    returns the result of multiplying it by the multiplier.
    """
    def multiplier_func(n: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Parameters:
        n (float): The float to multiply.

        Returns:
        float: The result of multiplying n by the multiplier.
        """
        return n * multiplier
    return multiplier_func
