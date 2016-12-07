#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# @ + 函数名
# 功能: 1.自动执行这个函数,并且将下面的函数名f1当做参数传递
#      2.将outer函数的返回值,重新赋值给放f1
def outer(func):
    def inner():
        print('log')
        return func()  # func() == f1原函数
    return inner    # 然后把封装后的函数输出给原函数 (= f1)

@outer
def f1():           #  == def inner():
    print("F1")     #        print('log')
                    #        func()

f1()


# @outer
# def f2():
#     print("F2")
#


# def f1():
#     print(123)
#
# def f1():
#     print(456)
#
# f1()

# def f1():
#     print("123")
#
# def f2(xxx):
#     xxx()
#
# f2(f1)

# #  装饰函数使用参数
# def outer(func):
#     def inner(name):      # func对应f1,f1有参数,这里也要接收参数好传递给内部funce
#         print("before")
#         r = func(name)
#         print("after")
#         return r  # 不要丢弃原函数返回值
#     return inner
#
#
# @outer
# def f1(arge):
#     print(arge)
#     return "F1"
#
# ret = f1('test')
# print(ret)


# #  装饰器装饰动态参数函数
# def outer(func):
#     def inner(*arge, **kwargs):   # 装饰器使用动态参数,来应对装饰不同得函数参数不确定情况
#         print("before")
#         r = func(*arge, **kwargs)  # 将原原函数的参数传递进来
#         print("after")
#         return r  # 不要丢弃原函数返回值
#     return inner
#
#
# @outer
# def f1(a1):
#     print(a1)
#     return "F1"
#
# @outer
# def f2(a1, b1):
#     print(a1, b1)
#     return "F2"
#
# print(f1('test1'))
#
# print(f2('test1', 'test2'))



# LOGIN_USER = {"is_login": False}
#
# def outer(func):
#     def inner(*arge, **kwargs):
#         if LOGIN_USER['is_login']:
#             r = func()
#             return r
#         else:
#             print("请登录")
#     return inner
#
#
# @outer
# def order():
#     print("欢迎登录成功")
#
# order()
