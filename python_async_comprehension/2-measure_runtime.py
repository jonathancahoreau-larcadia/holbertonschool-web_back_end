#!/usr/bin/env python3

"""Measure async comprehension runtime."""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure how long it takes to start four async comprehensions.

    Returns:
        Float: Total elapsed time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end = time.perf_counter()

    return end - start
