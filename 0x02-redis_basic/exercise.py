#!/usr/bin/env python3
"""module for redis basic"""
import redis
import uuid from uuid4
from typing import Union, Callable, Optional
from functools import wraps
UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """decorator counts how many times methods of Cache are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, *kwds):
        """wrapper function for count_calls method"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """decorator stores history of inputs and outputs"""
    input_list = method.__qualnmae__ + ":inputs"
    output_list = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args) -> bytes:
        """wrapper function for call_history method"""
        self._redis.rpush(input_list, str(args))
        output = method(self, *args)
        self._redis.rpush(output_list, output)
        return output
    return wrapper
    

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

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> UnionOfTypes:
        """retrieves data stored at key in desired format"""
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, data: str) -> str:
        """parametizes data to correct function, str"""
        return self.get(key, str)

    def get_int(self, data: str) -> int:
        """pararmetizes data to int"""
        return self.get(key, int)
