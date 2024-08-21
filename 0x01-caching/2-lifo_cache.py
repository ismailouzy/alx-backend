#!/usr/bin/env pyhon3
"""
lifo cache
"""


from threading import RLock
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    An implementation of LIFO (Last In First Out) Cache
    Attributes:
        __keys (list): Stores cache keys in order of entry using `.append`
        __rlock (RLock): Lock accessed resources to prevent race condition
    """
    def __init__(self):
        """ Instantiation method, sets instance attributes
        """
        super().__init__()
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            with self.__rlock:
                if key in self.__keys:
                    self.__keys.remove(key)
                self.__keys.append(key)
                self.cache_data[key] = item
                if len(self.__keys) > BaseCaching.MAX_ITEMS:
                    key_to_discard = self.__keys.pop(len(self.__keys) - 2)
                    del self.cache_data[key_to_discard]
                    print(f"DISCARD: {key_to_discard}")

    def get(self, key):
        """ Get an item by key
        """
        with self.__rlock:
            return self.cache_data.get(key, None)
