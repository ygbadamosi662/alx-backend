#!/usr/bin/env python3
"""
LIFOCache module
"""
from base_caching import BaseCaching
from typing import Any, Union


class LIFOCache(BaseCaching):
    """
    A class that uses last in first out for caching

    Args:
        BaseCaching (class): the base caching model
    """

    def __init__(self):
        """
        Initiliaze the base
        """
        super().__init__()

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key: str, item: Any):
        """ Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > self.MAX_ITEMS:
            first = sorted(self.cache_data.keys())[0]
            self.cache_data.pop(first)
            print('DISCARD: {}'.format(first))

    def get(self, key: str) -> Union[None, Any]:
        """ Get an item by key
        """
        if key and (key in self.cache_data.keys()):
            return self.cache_data.get(key)
        return None
