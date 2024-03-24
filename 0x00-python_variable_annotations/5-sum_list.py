#!/usr/bin/env python3

import typing

"""
This module provides a function to sum a list of floating-point numbers.

The sum_list function takes one parameter, a list of floats,
and returns their sum as a float.
This module is designed to be imported and used in other Python scripts.
"""


def sum_list(input_list: typing.List[float]) -> float:
    """
    Sums a list of floating-point numbers and returns the result as a float.

    Parameters:
    input_list (typing.List[float]):The list of floating-point
    numbers to sum.

    Returns:
    float: The sum of the numbers in input_list.
    """
    return sum(input_list)
