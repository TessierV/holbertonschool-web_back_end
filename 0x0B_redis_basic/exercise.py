#!/usr/bin/env python3
""" Writing strings to Redis """
from redis.client import Redis
from typing import Union
import uuid


class Cache:
    """ A class for caching data in Redis. """
    def __init__(self):
        """ Initialize the Cache class. """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


if __name__ == '__main__':
    cache = Cache()
