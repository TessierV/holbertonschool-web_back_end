#!/usr/bin/env python3
"""
function wait_n
:max_delay: int: 10
:n: int
:return: delay list in float
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    function wait_n
    :max_delay: int: 10
    :n: int
    :return: delay list in float
    """
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
