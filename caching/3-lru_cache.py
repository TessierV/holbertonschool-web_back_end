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
        self.order = []

    def put(self, key, item):
        """
        put
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        get the cache item value
        :return: cache_data value
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
