#!/usr/bin/env python3
"""
async_comprehension
:return: list of float
"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension
    :return: list of float
    """
    return [_ async for _ in async_generator()]
