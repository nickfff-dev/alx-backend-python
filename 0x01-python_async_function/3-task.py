#!/usr/bin/env python3
""" Module defines a function that Creates and returns an asyncio.Task """
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that,
    when awaited, will execute the wait_random coroutine.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - asyncio.Task: The task that, when awaited,
    will execute the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
