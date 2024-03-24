#!/usr/bin/env python3

"""
This module provides a function to convert a key-value pair into a tuple.

The to_kv function takes two parameters: a string key and a value that
can be an integer or float. It returns a tuple where the first element
is the key and the second element is the square of the value,
annotated as a float.
This module is designed to be imported and used in other Python scripts.
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Converts a key-value pair into a tuple where the first element is
    the key and the second element is the square of the value.

    Parameters:
    k (str): The key.
    v (typing.Union[int, float]): The value, which can be
    an integer or float.

    Returns:
    typing.Tuple[str, float]: A tuple containing the key
    and the square of the value.
    """
    return k, v**2
