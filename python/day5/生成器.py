#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# def func():
#     print(111)
#     yield 1
#     print(222)
#     yield 2
#     print(333)
#     yield 3
#
# ret = func()
# # print(ret)
#
# r1 = ret.__next__()
# print(r1)
# r2 = ret.__next__()
# print(r2)
# r3 = ret.__next__()
# print(r3)



def myrange(arg):
    start = 0
    while True:
        if start > arg:
            return
        yield start
        start += 1

ret = myrange(3)
r1 = ret.__next__()
print(r1)
r2 = ret.__next__()
print(r2)
r3 = ret.__next__()
print(r3)
r4 = ret.__next__()
print(r4)

ret = myrange(3)
for item in ret:
    print(item)





