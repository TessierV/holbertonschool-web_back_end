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

    def get(self, key: str, fn: Optional[Callable] = None) -> str:
        """
        Get
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Get string
        """
        value = self._redis
        return value.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> str:
        """
        Get int
        """
        value = self._redis
        return value.get(key, fn=int)

    def _generate_key(self):
        return str(uuid.uuid4())
