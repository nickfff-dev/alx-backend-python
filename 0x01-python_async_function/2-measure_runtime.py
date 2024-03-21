#!/usr/bin/env python3
""" Module defines a function that
Measures the total execution time for wait_n """
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call.

    Parameters:
    - n (int): The number of times to spawn wait_random.
    - max_delay (float): The maximum delay in seconds
    for each wait_random call.

    Returns:
    - float: The average time per call in seconds.
    """
    total_time: float
    # Start the timer
    start_time = time.perf_counter()

    # Run wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))

    # Calculate the total execution time
    total_time = time.perf_counter() - start_time

    # Return the average time per call
    return total_time / n
