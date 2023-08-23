#!/usr/bin/env python3
"""
    Defines LFUCache class
"""
from typing import Dict, Any, Optional as Opt
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        a class that cache using the Most Recently Used
        caching algorithm
        Args:
            BaseCaching (class): Base caching model
    """
    def __init__(self) -> None:
        """
            initialize the base and variable
        """
        super().__init__()
        self.freq: Dict[str, int] = {}

    def update_freq(self, key: str, value: Opt[Any]) -> None:
        """
            update the key value in the freq dict with 1 or
            assign if not present
            Args:
                key (str): key string
                value (Opt[Any]): the value of the key to append
        """
        if self.freq.get(key):  # check if the key is avail then incre
            self.freq[key] += 1
        else:
            self.freq[key] = 1
        self.cache_data[key] = value

    def put(self, key: str, item: Any) -> None:
        """
            assign key to value in the cache dict
        Args:
            key (str): the key in string
            item (Any): the value
        """
        if key and item:
            self.update_freq(key, item)
        if len(self.cache_data) > self.MAX_ITEMS:
            # remove the recently added key from self.freq to exclude it
            # from being used to calculate the least
            self.freq.pop(key)
            least: str = min(self.freq, key=lambda k: self.freq[k])
            self.cache_data.pop(least)
            self.freq.pop(least)
            self.freq[key] = 1  # then add it back after
            print("DISCARD: {}".format(least))

    def get(self, key: str) -> Opt[Any]:
        """
            get the data with the provided key.

            Args:
                key (str): the key

            Returns:
                Optional[Any]: value with any data type
        """
        if key:
            if self.cache_data.get(key):
                self.freq[key] += 1
            return self.cache_data.get(key)
        return None
