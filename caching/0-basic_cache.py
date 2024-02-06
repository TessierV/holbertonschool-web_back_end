#!/usr/bin/python3
""" BasicCache """

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        if key is not None:
            self.cache_data[key] = item

    def get(self, key):
        return self.cache_data.get(key, None)