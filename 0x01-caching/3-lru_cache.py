#!/usr/bin/env python3
"""
    A class that applies LRU caching system
"""
from typing import Any, Optional
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
        a class that cache using the Least Recently Used
        caching algorithm
        Args:
            BaseCaching (class): Base caching model
    """
    def __init__(self) -> None:
        """
            initialize the base and variable
        """
        super().__init__()

    def update(self, key: str, value: Any) -> None:
        """
            update the key value in the cache dict and add it
            to the last of the dict as recent.
            Args:
                key (str): key string
                value (Any): the value of the key to append
        """
        if self.cache_data.get(key):  # check if the key is avail then pop
            self.cache_data.pop(key)
        self.cache_data[key] = value

    def put(self, key: str, item: Any) -> None:
        """
            assign key to value in the cache dict
        Args:
            key (str): the key in string
            item (Any): the value
        """
        if key and item:
            self.update(key, item)
        if len(self.cache_data) > self.MAX_ITEMS:
            least: str = list(self.cache_data.keys())[0]
            self.cache_data.pop(least)
            print("DISCARD: {}".format(least))

    def get(self, key: str) -> Optional[Any]:
        """
            get the data with the provided key.

            Args:
                key (str): the key

            Returns:
                Optional[Any]: value with any data type
        """
        if key:
            if self.cache_data.get(key):
                self.update(key, self.cache_data.get(key))
            return self.cache_data.get(key)
        return None
