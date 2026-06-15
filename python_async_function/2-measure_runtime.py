#!/usr/bin/env python3

"""Measure the average runtime of concurrent async coroutines."""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run wait_n and return the average execution time per coroutine.

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay passed to wait_n.

    Returns:
        float: Average runtime in seconds per coroutine.
    """

    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    runtime = end - start
    return runtime / n
