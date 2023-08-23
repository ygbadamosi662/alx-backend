#!/usr/bin/env python3
"""
MRUCache  module
"""
from base_caching import BaseCaching
from typing import Any, Union


class MRUCache (BaseCaching):
    """
    a class that cache using the Most Recently Used
    caching algorithm
    Args:
        BaseCaching (class): Base caching model
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

    def update_key(self, key: str, item: Any):
        """
            update the key value in the cache dict and add it
            to the last of the dict as recent.
            Args:
                key (str): key string
                item (Any): the value of the key to append
        """
        if key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.cache_data[key] = item

    def put(self, key: str, item: Any):
        """ Add an item in the cache
        """
        if key and item:
            self.update_key(key, item)

        if len(self.cache_data) > self.MAX_ITEMS:
            recently_used: str = list(self.cache_data.keys())[-2]
            self.cache_data.pop(recently_used)
            print('DISCARD: {}'.format(recently_used))

    def get(self, key: str) -> Union[None, Any]:
        """ Get an item by key
        """
        if key and (key in self.cache_data.keys()):
            return self.cache_data.get(key)
        return None
