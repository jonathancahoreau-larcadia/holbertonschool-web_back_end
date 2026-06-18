#!/usr/bin/env python3

"""Entry point for measuring asynchronous runtime.

This module runs the `measure_runtime` coroutine from
`2-measure_runtime.py` and prints its result. It is intended
as a small runner for demonstration and testing purposes.
"""

import asyncio


measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    """Run and return the result of the `measure_runtime` coroutine."""
    return await(measure_runtime())


print(asyncio.run(main()))
