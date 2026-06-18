#!/usr/bin/env python3
"""Asynchronous helper for delaying a random amount of time."""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
