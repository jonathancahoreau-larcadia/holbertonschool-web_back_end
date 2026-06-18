#!/usr/bin/env python3

"""Asynchronously collect values from an async generator."""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List:
    """Collect all values from async_generator into a list.

    Returns:
        list[float]: Values gathered from the async generator.
    """
    result = []
    async for number in async_generator():
        result.append(number)

    return result
