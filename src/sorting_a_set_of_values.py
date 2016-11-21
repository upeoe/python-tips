#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fn01():
    """sorted() will return a new sorted list"""
    s = {7, 3, 5, 1, 6}
    print('before sorted: {0}, type: {1}'.format(s, type(s)))
    d = sorted(s)
    print('after sorted {0}, type: {1}'.format(d, type(d)))


if __name__ == '__main__':
    fn01()
