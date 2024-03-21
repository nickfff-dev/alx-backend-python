#!/usr/bin/env python3
""" Module defines a function that
Measures the total execution time for wait_n """
import asyncio
import random
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
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

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start_time
    return total_time / n
