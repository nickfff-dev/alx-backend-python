#!/usr/bin/env python3
"""
This module provides a coroutine that
collects 10 random numbers using an async comprehension
over the async_generator from the previous task,
then returns the 10 random numbers.
"""
from typing import List
import asyncio


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension
    over the async_generator,
    then returns the 10 random numbers as a list.
    """
    # Using an async list comprehension to collect the numbers
    numbers = [number async for number in async_generator()]
    return numbers
