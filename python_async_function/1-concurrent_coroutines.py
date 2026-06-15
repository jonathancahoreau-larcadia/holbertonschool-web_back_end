#!/usr/bin/env python3

"""Asynchronous coroutine utilities for concurrent delays."""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn async wait_random coroutines and return delays
    in completion order.

    Args:
        n (int): Number of coroutines to run concurrently.
        max_delay (int): Maximum random delay for each coroutine.

    Returns:
        List[float]: Sorted list of delays as coroutines complete.
    """

    tasks = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    list_sorted = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_sorted.append(delay)
    return list_sorted
