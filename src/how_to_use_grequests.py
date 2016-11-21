#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import grequests


def fn01():
    urls = [
        'http://www.baidu.com/s?wd=upeoe',
        'http://www.baidu.com/s?wd=test',
        'http://www.baidu.com/s?wd=lol'
    ]

    rs = (grequests.get(u) for u in urls)
    print(type(rs))
    for resp in grequests.map(rs):
        if resp is not None:
            print('status:{0} url:{1}'.format(resp, resp.url))


def fn02():
    urls = [
        'http://www.baidu.com/s?wd=upeoe',
        'http://www.baidu.com/s?wd=test',
        'http://www.baidu.com/s?wd=lol',
        'http://someaddr.com/',
        'http://httpbin.org/status/500'
    ]

    rs = (grequests.get(u) for u in urls)
    for resp in grequests.map(rs, exception_handler=exception_handler):
        if resp is not None:
            print('status:{0} url:{1}'.format(resp, resp.url))


def exception_handler(request, exception):
    print('got exception url: {0}, exception {1}'.format(request.url, exception))


if __name__ == '__main__':
    fn01()
    fn02()
