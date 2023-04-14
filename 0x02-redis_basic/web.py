#!/usr/bin/env python3
"""
Web file
"""
import requests
import redis
from functools import wraps

store = redis.Redis()


def count_url_access(method):
    """ Counting how many times
    a Url is accessed """
    @wraps(method)
    def wrapper(url):
        cached = "cached:" + url
        cached_data = store.get(cached)
        if cached_data:
            return cached_data.decode("utf-8")

        count = "count:" + url
        html = method(url)

        store.incr(count)
        store.set(cached, html)
        store.expire(cached, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text
