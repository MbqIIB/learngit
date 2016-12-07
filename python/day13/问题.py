#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5


# 方法二：manage.dict()共享数据
from multiprocessing import Process, Manager
# 不明白Manager
manage = Manager()
dic = manage.dict()


def Foo(i):
    dic[i] = 100+i
    print(dic.values())

for i in range(2):
    p = Process(target=Foo, args=(i,))
    p.start()
    p.join()

# monkey (?)
from gevent import monkey; monkey.patch_all()
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))


gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.com/'),
    gevent.spawn(f, 'https://www.github.com/'),
])


