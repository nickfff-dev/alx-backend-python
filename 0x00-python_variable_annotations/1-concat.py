#!/usr/bin/env python3

"""
This module provides a function to concatenate two strings.

The concat function takes two parameters, both of type str,
and returns their concatenation as a str.
This module is designed to be imported and used in other Python scripts.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result.

    Parameters:
    str1 (str): The first string to concatenate.
    str2 (str): The second string to concatenate.

    Returns:
    str: The concatenation of str1 and str2.
    """
    return str1 + str2
