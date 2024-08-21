#!/usr/bin/env python3
"""
basic dict
"""


class BasicCache(BaseCaching):
    """
    A basic caching system that inherits from
    BaseCaching and doesn't have a limit.
    """
    def put(self, key, item):
        """
        Add an item in the cache with a specific key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache by key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
