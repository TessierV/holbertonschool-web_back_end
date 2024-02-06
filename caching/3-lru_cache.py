#!/usr/bin/python3
"""
LRUCache
:return: cache_data
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache
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
                lru_key = list(self.cache_data.keys())[-1]
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get
        :return: cache_data
        """
        if key is not None and key in self.cache_data:
            self.order_used.remove(key)
            self.order_used.append(key)
            return self.cache_data[key]
        return None

