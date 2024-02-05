#!/usr/bin/env python3
# countasync.py
import asyncio
import random

"""
function wait_random
:max_delay: int: 10
:return: delay in float
"""

async def wait_random(max_delay: int = 10) -> float:
    """
    function wait_random
    :max_delay: int: 10
    :return: delay in float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay