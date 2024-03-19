#!/usr/bin/env python3
"""
Module for defining a Cache class using Redis.
"""
from redis.client import Redis
import redis
from typing import Union
import uuid


class Cache:
    """
    Module for defining a Cache class using Redis.
    """
    def __init__(self):
        """
        Module for defining a Cache class using Redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Module for defining a Cache class using Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
