#!/usr/bin/env python3
"""
This module provides a
coroutine that measures the total runtime of executing
async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.
    """
    # Create a list of four async_comprehension coroutines
    tasks = [async_comprehension() for _ in range(4)]

    # Start the execution of all tasks in parallel
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()

    # Calculate and return the total runtime
    total_runtime = end_time - start_time
    return total_runtime
