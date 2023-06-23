#!/usr/bin/env python3
'''Redis cache'''


import requests
import redis
from typing import Callable
from functools import wraps


def call_count(fn: Callable) -> Callable:
    '''track how many times a
    particular URL was accessed
    in the key "count:{url}" and
    cache the result with an
    expiration time of 10 seconds'''

    @wraps(fn)
    def wrapper(url):
        '''wrapper function'''
        r = redis.Redis()

        cache_key = 'cache:{}'.format(url)
        cache_value = r.get(cache_key)
        if cache_value:
            return cache_value.decode('utf-8')

        # get_page if url is no cache or expired
        key = 'count:{}'.format(url)
        html_content = fn(url)

        r.incr(key)
        r.set(cache_key, html_content)
        r.expire(cache_key, 10)
        return html_content

    return wrapper


@call_count
def get_page(url: str) -> str:
    '''returns the HTML content of a particular URL'''
    result = requests.get(url)
    return result.text
