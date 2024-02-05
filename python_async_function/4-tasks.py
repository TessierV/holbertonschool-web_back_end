#!/usr/bin/env python3
"""
task_wait_n
:n: int
:max_delay: int: 10
:return: list of float
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    task_wait_n
    :n: int
    :max_delay: int: 10
    :return: list of float
    """
    list_float = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(list_float)
