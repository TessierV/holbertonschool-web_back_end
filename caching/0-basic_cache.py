#!/usr/bin/python3
"""
BasicCache
:return: cache_data
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache
    :return: cache_data
    """
    def put(self, key, item):
        """
        Put
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get
        :return: cache_data
        """
        return self.cache_data.get(key, None)
