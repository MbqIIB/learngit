#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

str1 = 'luotianshuai'
str2 = str1
print(id(str1))
print(id(str2))
print('===========================')
str1 = 'shuaige'
print(id(str1))
print(id(str2))
