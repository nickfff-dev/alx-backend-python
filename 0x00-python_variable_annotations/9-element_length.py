#!/usr/bin/env python3

"""
This module provides a function to calculate the
length of each element in a list.

The element_length function takes one parameter,
a list of sequences, and returns a list of tuples where
each tuple contains an element from the list and its length.
This module is designed to be imported and used in other Python scripts.
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Calculates the length of each element in a list
    and returns a list of tuples.

    Parameters:
    lst (typing.Iterable[typing.Sequence]): The list of sequences
    to calculate the length of each element.

    Returns:
    typing.List[typing.Tuple[typing.Sequence, int]]: A list of tuples
    where each tuple contains an element from the list and its length.
    """
    return [(i, len(i)) for i in lst]
