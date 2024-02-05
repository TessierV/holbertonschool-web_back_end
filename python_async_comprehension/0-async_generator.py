#!/usr/bin/env python3
import asyncio
import random
from typing import Generator
"""
async_generator
:n: int
:max: 10
"""


async def async_generator():
    """
    async_generator
    :generator: float, none, none
    :max: 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
