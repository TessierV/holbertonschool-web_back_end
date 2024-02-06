#!/usr/bin/python3
"""
FIFOCache
:return: cache_data
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache
    :return: cache_data
    """
    def __init__(self):
        """
        init
        """
        super().__init__()

    def put(self, key, item):
        """
        put
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get
        :return: cache_data
        """
        return self.cache_data.get(key, None)
