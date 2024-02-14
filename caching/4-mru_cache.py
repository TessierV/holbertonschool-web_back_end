#!/usr/bin/python3
"""
MRUCache
:return: cache_data
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache
    :return: cache_data
    """
    def __init__(self):
        """
        init
        """
        self.timesKey = {}
        self.time = 0
        super().__init__()

    def put(self, key, item):
        """
        put
        """
        if key is not None and item is not None:
            self.timesKey[key] = self.time
            self.time += 1

            self.cache_data[key] = item

        while len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard_key = min(self.timesKey, key=self.timesKey.get)
            self.cache_data.pop(discard_key)
            self.timesKey.pop(discard_key)

            print("DISCARD:", discard_key)

    def get(self, key):
        """
        get the cache item value
        :return: cache_data value
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
