#!/usr/bin/env python3
"""
lifo caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching and
    implements the LIFO (Last-In-First-Out) eviction policy.
    """
    def __init__(self):
        """
        Initialize the cache.
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item in the cache with a specific key.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
