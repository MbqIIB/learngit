#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

USER_INFO = {'is_login': None, 'user_type': 1}
# USER_INFO['is_login']
# USER_INFO.get('is_login', None)


def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('is_login', None):
            ret = func(*args, **kwargs)
            return ret
        else:
            print("请登录!")
    return inner


def check_admin(func):
    def inner(*args, **kwargs):
        if USER_INFO.get('user_type', None) == 2:
            ret = func(*args, **kwargs)
            return ret
        else:
            print('无权查看')
    return inner


@check_login
@check_admin
def index():
    """
    管理员的功能
    :return:
    """
    print('Index')


------------------------华丽的分割线-----------------------------


# 装饰器装饰也是有顺序的,代码是从上到下加载到内存中,
# 我们知道装饰器会把被 [@装饰器] 下面的函数装饰,并将它当作参数传递到装饰器里面.
# 装饰顺序结构(0),(1),(2)  (0)代表被装饰函数本体
@check_login
@check_admin
def index():
    """
    管理员的功能
    :return:
    """
    print('Index')



if USER_INFO.get('is_login', None):   # (2) check_login函数体
    if USER_INFO.get('user_type', None) == 2:  # (1) check_admin函数体
        ret = print('Index')  # (0) index函数本体
        return ret            # (0) index函数返回值
    else:
        print('无权查看')  # (1) check_admin函数体
else:
    print("请登录!")   # (2) check_login函数体







