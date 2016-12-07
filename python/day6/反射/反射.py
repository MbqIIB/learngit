#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 反射:利用字符串的形式去对象中(模块)中操作(查找/检测/添加/删除)成员
# import commons
# __import__("lib.account")   # 接受字符串得形式导入模块


def run():
    # account/login
    inp = input("请输入访问页面:")
    m, f = inp.split('/')
    obj = __import__('lib.' + m, fromlist=True)
    if hasattr(obj, f):           # 判断这个模块中是否有这个函数
        func = getattr(obj, f)    # 得到这个对象
        func()
    else:
        print("404")


if __name__ == '__main__':
    run()

