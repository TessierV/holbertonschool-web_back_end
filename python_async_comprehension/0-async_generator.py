#!/usr/bin/env python3
"""
async_generator
:n: int
:max: 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async_generator
    :generator: float, none, none
    :max: 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
