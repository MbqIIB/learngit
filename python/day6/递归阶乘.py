#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 1*2*3*4*5*6*7
def func(num):
    if num == 1:
        return 1
    return num * func(num-1)

x = func(7)
print(x)

