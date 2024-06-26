#!/usr/bin/env python3
""" Module defines function wait_ random; An asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    An asynchronous coroutine that waits for a
    random delay between 0 and max_delay seconds.

    Parameters:
    - max_delay (float): The maximum delay in seconds. Default is 10.

    Returns:
    - float: The actual delay that was waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
