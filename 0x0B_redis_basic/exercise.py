#!/usr/bin/env python3
"""
Writing strings to Redis
"""
from redis.client import Redis
import redis
from typing import Union
import uuid


class Cache:
    """
    Class Cache.
    """
    def __init__(self):
        """
        Init
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
