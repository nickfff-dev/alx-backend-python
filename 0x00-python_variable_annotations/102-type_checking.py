#!/usr/bin/env python3
""" This Module defines a function that
Safely retrieves a value from a dictionary by key
"""

from typing import List, Tuple, TypeVar, Union

T = TypeVar('T')


def zoom_array(lst: List[T], factor: int = 2) -> List[T]:
    """
    Zooms an array by repeating each element a specified number of times.

    Parameters:
    lst (List[T]): The list to zoom.
    factor (int, optional): The number of times to repeat each element.
    Defaults to 2.

    Returns:
    List[T]: The zoomed list.
    """
    zoomed_in: List[T] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
