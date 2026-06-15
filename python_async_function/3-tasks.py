#!/usr/bin/env python3

"""Asynchronous task helper for random delay coroutines."""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create and return an async task running wait_random.

    Args:
        max_delay (int): Maximum delay for the random wait.

    Returns:
        asyncio.Task[float]: Task executing wait_random with the given delay.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
