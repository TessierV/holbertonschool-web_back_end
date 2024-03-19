#!/usr/bin/env python3
""" Writing strings to Redis """
from redis.client import Redis
from typing import Union
import uuid


class Cache:
    """ class """
    def __init__(self):
        """ init """
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

if __name__ == '__main__':
    main()
