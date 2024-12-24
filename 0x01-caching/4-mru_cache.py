#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class
        A caching system using the MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache exceeds the max limit, remove the
                # most recently used item
                # Get the last inserted key
                mru_key = list(self.cache_data.keys())[-1]
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end (most recently used)
        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item

        return item
