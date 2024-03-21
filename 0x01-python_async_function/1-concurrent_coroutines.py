#!/usr/bin/env python3
""" Module defines An asynchronous
coroutine that spawns wait_random n times """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    An asynchronous coroutine that spawns wait_random n
    times with the specified max_delay.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (float): The maximum delay in seconds for
    each wait_random call.

    Returns:
    - List[float]: A list of all the delays in ascending order.
    """
    # Create a list of tasks to run concurrently
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Gather the results of all tasks
    results = await asyncio.gather(*tasks)

    # Initialize an empty list to store the delays in ascending order
    delays = []

    # Iterate over the results and insert each delay into its correct position
    for delay in results:
        # Find the correct position for the current delay
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    return delays
