#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

import requests


def fn01():
    """
    Problem: ValueError: Expecting value: line 1 column 1 (char 0)

    expect this response data like '{"a": 1}'
    when using json.loads(), it will raise an error
    if you print this data, you will see `b'{"a": 1}'`
    if using a tool such as `curl -v` to test
    you will get: `Content-Type: application/json; charset=utf-8`
    Reason: Python considered this data is byte stream,
    but it encoded as utf-8 indeed
    so we should convert it at first
    """
    r = requests.get('http://response.json.com')
    print(r.content)
    print(type(r.content))
    json.loads(str(r.content))


def fn02():
    # now it works
    r = requests.get('http://response.json.com')
    s1 = r.content.decode('utf-8')
    # or
    s2 = str(r.content, 'utf-8')
    json.loads(s1)
    json.loads(s2)
