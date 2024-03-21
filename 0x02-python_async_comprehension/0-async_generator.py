#!/usr/bin/env python3
"""
This module provides an asynchronous generator
that yields random numbers between 0 and 10,
with a 1-second delay between each yield,
for a total of 10 yields.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yields a random number between
    0 and 10, 10 times, with a 1-second delay
    between each yield. This coroutine is useful
    for simulating asynchronous data generation
    in a controlled manner.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
