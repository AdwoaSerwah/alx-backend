#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache class
        A caching system using the LFU (Least Frequently Used) algorithm.
    """

    def __init__(self):
        """ Initialize the LFUCache
        """
        super().__init__()
        self.frequency = defaultdict(int)  # Tracks frequency of keys
        self.order = defaultdict(list)  # Tracks keys in order of use
        self.key_to_time = {}  # Tracks the time keys were last used

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find the least frequently used key (LFU)
            min_freq = min(self.frequency.values(), default=None)
            lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]

            # If there are multiple keys with the same frequency, apply LRU
            if len(lfu_keys) > 1:
                lru_key = min(lfu_keys, key=lambda k: self.key_to_time[k])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.key_to_time[lru_key]
                print(f"DISCARD: {lru_key}")
            else:
                lfu_key = lfu_keys[0]
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.key_to_time[lfu_key]
                print(f"DISCARD: {lfu_key}")

        # Add the new key
        self.cache_data[key] = item
        self.frequency[key] = 1
        self.order[key] = [key]
        self.key_to_time[key] = len(self.key_to_time)  # Update time stamp

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and time of last use
        self.frequency[key] += 1
        self.key_to_time[key] = len(self.key_to_time)
        return self.cache_data[key]
