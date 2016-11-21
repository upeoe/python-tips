#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time


def fn01():
    """return the current local date and time"""
    print(datetime.datetime.today())
    start = datetime.datetime.now()
    run()
    end = datetime.datetime.now()
    spend = end - start
    print('spend:{0}, seconds:{1}, microseconds:{1}'.format(spend, spend.seconds, spend.microseconds))


def fn02():
    """return the current time as a float value"""
    start = time.time()
    run()
    end = time.time()
    print(end - start)


def fn03():
    """
    fn01(), fn02() 都包含其他程序使用CPU的时间
    fn03() 只计算当前程序运行的CPU时间
    """
    start = time.clock()
    run()
    end = time.clock()
    print(end - start)


def run():
    for i in range(1000):
        i += 1


if __name__ == '__main__':
    fn01()
    fn02()
    fn03()
