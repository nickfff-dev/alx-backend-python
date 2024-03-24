#!/usr/bin/env python3
""" This Module defines a function that
Safely retrieves a value from a dictionary by key
"""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms an array by repeating each element a specified number of times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(tuple(array))
zoom_3x = zoom_array(tuple(array), int(5.0))
