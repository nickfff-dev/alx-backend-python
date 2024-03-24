#!/usr/bin/env python3

"""
This module provides a function to safely retrieve
the first element of a list.

The safe_first_element function takes one parameter,
a list, and returns the first element of the list
if it exists, otherwise it returns None.
This module is designed to be imported and used in other Python scripts.
"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Optional[typing.Any]:
    """
    Safely retrieves the first element of a list.

    Parameters:
    lst (typing.Sequence[typing.Any]): The list from which to retrieve
    the first element.

    Returns:
    typing.Optional[typing.Any]: The first element of the list if it exists,
    otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
