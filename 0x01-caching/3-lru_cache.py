#!/usr/bin/env python3
"""
LRU caching
"""

from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching and
    implements the LRU (Least Recently Used) eviction policy.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache with a specific key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_recent_key = next(iter(self.cache_data))
            print(f"DISCARD: {least_recent_key}")
            del self.cache_data[least_recent_key]

    def get(self, key):
        """
        Get an item from the cache by key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
