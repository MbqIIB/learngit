#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# # 通过对系统标准输入监控来得到每次屏幕输入的内容
# import select
# import sys
#
# while True:
#     readable, writeable, error = select.select([sys.stdin, ], [], [], 1)
#     if sys.stdin in readable:
#         print('select get stdin', sys.stdin.readline())



