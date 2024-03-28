#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional

class Cache:
    """
    Class Cache.
    """
    def __init__(self):
        """Initialize Redis connection."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def _generate_key():
        """Generate a unique key."""
        return str(uuid.uuid4())

    @staticmethod
    def _decode_value(value: bytes) -> str:
        """Decode value to string."""
        return value.decode("utf-8")

    @staticmethod
    def _parse_int(value: bytes) -> int:
        """Parse value to integer."""
        try:
            return int(value.decode("utf-8"))
        except ValueError:
            return 0

    @staticmethod
    def _format_output(key: str, value: bytes) -> str:
        """Format function output."""
        return "{}(*{}) -> {}".format(key, value.decode("utf-8"), value.decode("utf-8"))

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data from Redis."""
        value = self._redis.get(key)
        return value if not fn else fn(value)

    def get_str(self, key: str) -> str:
        """Retrieve string data from Redis."""
        return self.get(key, self._decode_value)

    def get_int(self, key: str) -> int:
        """Retrieve integer data from Redis."""
        return self.get(key, self._parse_int)


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a particular function."""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapped function."""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Count how many times methods of the Cache class are called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapped function."""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def replay(method: Callable):
    """Display the history."""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis_instance = method.__self__._redis
    count = redis_instance.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    input_list = redis_instance.lrange(inputs, 0, -1)
    output_list = redis_instance.lrange(outputs, 0, -1)
    redis_data_pairs = list(zip(input_list, output_list))

    for input_data, output_data in redis_data_pairs:
        input_str, output_str = input_data.decode("utf-8"), output_data.decode("utf-8")
        print("{}(*{}) -> {}".format(key, input_str, output_str))
