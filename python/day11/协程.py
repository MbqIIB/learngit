#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# from greenlet import greenlet
#
#
# def test1():
#     print(12)      # (1)
#     gr2.switch()   # 遇到这个跳到下一个
#     print(34)      # (3)
#     gr2.switch()
#
#
# def test2():
#     print(56)      # (2)
#     gr1.switch()
#     print(78)      # (4)
#
# # 创建两个协程,协程运行遇到IO操作需要等待得时候执行另一个协程
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()  # 执行第一个协程
#
# '''
# 比I/O操作，如果10个I/O，我程序从上往下执行，如果同时发出去了10个I/O操作，那么返回的结果如果同时回来了2个
# ，是不是就节省了很多时间？
#
# 如果一个线程里面I/O操作特别多，使用协程是不是就非常适用了！
#
# 如果一个线程访问URL通过协程来做，协程告诉它你去请求吧，然后继续执行，但是如果不用协程就得等待第一个请求完毕之后返回之后才
# 继续下一个请求。
#
# 协程：把一个线程分成了多个协程操作，每个协程做操作
# 多线程：是把每一个操作，分为多个线程做操作，但是python中，在同一时刻只能有一个线程操作，并且有上下文切换。但是如果上下文切换非常频繁的话
# 是非常耗时的，但对于协程切换就非常轻便了~
# '''




from gevent import monkey; monkey.patch_all()
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),  # 这里的f是调用的任务,第二个是给这个任务传的参数
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://www.github.com/'),
])

'''
当遇到I/O操作的时候就会调用协程操作，然后继续往下走，然后这个协程就卡在这里等待数据的返回
'''
