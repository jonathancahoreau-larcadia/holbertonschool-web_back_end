#!/usr/bin/env python3

"""Asynchronously collect values from an async generator."""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect all values from async_generator using async comprehension.

    Returns:
        list[float]: Values gathered from the async generator.
    """
    return [number async for number in async_generator()]
