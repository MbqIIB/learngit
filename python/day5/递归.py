#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 递归演示
# def d():
#     return '123'
#
#
# def c():
#     r = d()
#     return r
#
#
# def b():
#     r = c()
#     return r
#
#
# def a():
#     r = b()
#     print(r)
#
# a()


def func(n):
    n += 1
    if n >= 4:
        print(n)
        return "end"
    return func(n)

r = func(1)  # 我传递进去个1,经过递归最后给我返回4
print(r)





