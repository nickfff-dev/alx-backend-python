#!/usr/bin/env python3

"""
This module provides a function to sum a list of integers and floats.

The sum_mixed_list function takes one parameter, a
list of integers and floats, and returns their sum as a float.
This module is designed to be imported and used in other Python scripts.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Sums a list of integers and floats and returns the result as a float.

    Parameters:
    mxd_lst (typing.List[typing.Union[int, float]]): The list of
    integers and floats to sum.

    Returns:
    float: The sum of the numbers in mxd_lst.
    """
    return sum(mxd_lst)
