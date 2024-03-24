#!/usr/bin/env python3
""" This Module defines a function that
Safely retrieves a value from a dictionary by key
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary by key,
    returning a default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
