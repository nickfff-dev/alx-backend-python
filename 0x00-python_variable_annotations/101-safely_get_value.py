#!/usr/bin/env python3
""" This Module defines a function that
Safely retrieves a value from a dictionary by key
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Optional[T] = None) -> Union[T, None]:
    """
    Safely retrieves a value from a dictionary by key,
    returning a default value if the key is not found.

    Parameters:
    dct (Mapping[Any, T]): The dictionary from which to
    retrieve the value.
    key (Any): The key to look for in the dictionary.
    default (Optional[T], optional): The default value to
    return if the key is not found in the dictionary. Defaults to None.

    Returns:
    Union[T, None]: The value associated with the key in the dictionary,
    or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
