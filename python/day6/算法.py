#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 冒泡排序
l = [2, 12, 8, 16, -3, 20]

# num = len(l)
# for i in range(num):

for i in l:
    for v in l:
        if i > v:
            i_index = l.index(i)
            v_index = l.index(v)
            l[i_index] = v
            l[v_index] = i

print(l)

