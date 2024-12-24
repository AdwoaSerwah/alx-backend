#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class
        A caching system using the LRU (Least Recently Used) algorithm.
    """

    def __init__(self):
        """ Initialize the LRUCache
        """
        super().__init__()
        self.order = []  # To keep track of the access order

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If the cache exceeds the max limit, remove the least
                # recently used item
                lru_key = self.order.pop(0)  # Remove the first element (LRU)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.order.append(key)  # Mark this key as recently used

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the order (recently used)
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
