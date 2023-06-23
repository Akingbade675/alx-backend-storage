#!/usr/bin/env python3
'''Redis with Python'''


import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''count how many times methods
    of the Cache class are called'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''the wrapper definition'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    '''decorator to store the history of inputs
    and outputs for a particular function'''
    name = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper function'''
        self._redis.rpush('{}:inputs'.format(name), str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush('{}:outputs'.format(name), output)
        return output

    return wrapper


def replay(fn: Callable):
    '''display the history of calls
    of a particular function'''
    name = fn.__qualname__
    r = redis.Redis()
    func_call_count = r.get(name).decode('utf-8')

    print('{} was called {} times:'.format(name, func_call_count))

    inputs = r.lrange('{}:inputs'.format(name), 0, -1)
    outputs = r.lrange('{}:outputs'.format(name), 0, -1)

    # decode binary to string format
    def decode(value): return value.decode('utf-8')

    for input, output in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, decode(input), decode(output)))


class Cache():
    '''Cache class'''

    def __init__(self):
        '''store an instance of the Redis client'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''generate a random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''convert data back to the desired format'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key) -> str:
        '''get string'''
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key) -> int:
        '''get int'''
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
