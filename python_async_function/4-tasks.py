#!/usr/bin/env python3

"""Asynchronous task utilities for concurrent random delays."""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create and await multiple async tasks, returning sorted delays.

    Args:
        n (int): Number of tasks to create and run concurrently.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: Sorted list of delays as tasks complete.
    """

    tasks = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    list_sorted = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        list_sorted.append(delay)
    return list_sorted
