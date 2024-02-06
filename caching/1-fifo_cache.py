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
    def put(self, key, item):
        """
        Put
        """
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order[0]
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Get
        :return: cache_data
        """
        return self.cache_data.get(key, None)
