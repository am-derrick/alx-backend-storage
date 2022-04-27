#!/usr/bin/env python3
"""module for redis basic"""

import redis
import uuid from uuid4
from typing import Union, Callable, Optional
UnionOfTypes = Union[str, bytes, int, float]


class Cache:
    """cache class storinginstance of redis client"""

    def __init__(self):
        """instance of redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: UnionOfTypes) -> str:
        """method generates a random key, stores input data in Redis"""
        key = str(uuid4())
        self.redis.mset({key: data})
        return key
