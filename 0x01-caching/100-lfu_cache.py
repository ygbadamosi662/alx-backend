#!/usr/bin/env python3
"""
LFUCache  module
"""
from base_caching import BaseCaching
from typing import Any, Union, Dict


class LFUCache (BaseCaching):
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
        self.freq_data: Dict[str, int] = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def update_freq(self, key: str, item: Any):
        """
            update the key value in the cache dict and add it
            to the last of the dict as recent.
            Args:
                key (str): key string
                item (Any): the value of the key to append
        """
        if key in self.freq_data.keys():
            self.cache_data.pop(key)
            self.freq_data[key] += 1
        else:
            self.freq_data[key] = 1

        self.cache_data[key] = item

    def put(self, key: str, item: Any):
        """ Add an item in the cache
        """
        if key and item:
            self.update_freq(key, item)

        if len(self.cache_data) > self.MAX_ITEMS:
            not_loved = []
            hold = 1

            for i in self.freq_data.keys():
                if i != key:
                    if self.freq_data.get(i) > hold:
                        hold = self.freq_data.get(i)

            for i in self.freq_data.keys():
                if (i != key) and (self.freq_data.get(i) == hold):
                    not_loved.append(i)

            if len(not_loved) == 1:
                least = not_loved[0]

            if len(not_loved) > 1:
                cache_keys = list(self.cache_data.keys())
                min_index = len(self.cache_data.keys())
                for i in not_loved:
                    if cache_keys.index(i) < min_index:
                        min_index = cache_keys.index(i)
                least = cache_keys[min_index]

            print('DISCARD: {}'.format(least))

    def get(self, key: str) -> Union[None, Any]:
        """ Get an item by key
        """
        if key and (key in self.cache_data.keys()):
            return self.cache_data.get(key)
        return None
