#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 遍历列表,将"9"全部替换成"999"
name = ['Alex', 'Jack', 'Rain', [9, 4, 3, 5], 9]

for num in name:
    if num == 9:
        key = name.index(num)
        name[key] = 9999
    elif type(num) == list:
        index = name.index(num)
        for num1 in num:
            if num1 == 9:
                index1 = num.index(num1)
                name[index][index1] = 9999
print(name)