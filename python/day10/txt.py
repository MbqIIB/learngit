#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# # 问题1
# aaa = {"k1": "v1"}
# try:
#     aaa["k11"]
# except KeyError as e:
#     print(e)
# #
# #
# #
# # ########### 单例类定义 ###########
# class Foo(object):
#
#     __instance = None
#
#     @staticmethod
#     def singleton():
#         if Foo.__instance:
#             return Foo.__instance
#         else:
#             Foo.__instance = Foo() # 创建对象,并__instance=对象
#             return Foo.__instance # 刚才创建的对象
#
# # ########### 获取实例 ###########
# obj = Foo.singleton()
# print(obj)
# Foo.singleton()

# 问题 class __init__(self): 不能retrun

# 元类
# class MyType(type):
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__()
#         obj.__init__()
#         return obj
#
# class Foo(metaclass=MyType):
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         ret = object.__new__(cls)
#         return ret
#
# obj = Foo()



#  python中无块级作用域,python中以函数为作用域
# if 1 == 1:
#     name = "alex"
#
# print(name)


# python代码还没执行的时候,作用域就已经形成了
# name = 'alex'
# def f1():
#     print(name)
#
#
# def f2():
#     name = 'eric'
#     f1()
# f2()
#
#
# # 烧脑新浪面试题
# # return x
# li = [lambda: x for x in range(10)]
# # li列表
# # li列表中的元素[函数,函数,函数,函数...]
# # 函数在没有执行前,内部代码不执行
# # ? li[0] ,函数
# # ? 函数()
# # 返回值是???
# r = li[0]()
# print(r)

# 《宇宙时空之旅》
