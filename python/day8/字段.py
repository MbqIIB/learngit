#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# # 一般情况:自己访问自己的字段
# # 规则:
# #     普通字段只能用对象访问
# #     静态字段用类访问(万不得已的时候使用对象访问)
# class Province:
#     country = "中国"
#
#     def __init__(self,name):
#         self.name = name
#
# hn = Province('湖南省')
#
# print(Province.country)
# print(hn.country)
# print(hn.name)


# class C:
#
#     name = "公有静态字段"
#
#     def func(self):
#         print(C.name)
#
# class D(C):
#
#     def show(self):
#         print(C.name)
#
#
# C.name         # 类访问
#
# obj = C()
# obj.func()     # 类内部可以访问
#
# obj_son = D()
# obj_son.show() # 派生类中可以访问



# class C:
#
#     def __init__(self):
#         self.__foo = "私有字段"
#
#     def func(self):
#         print(self.foo)   # 类内部访问
#
# class D(C):
#
#     def show(self):
#         print(self.foo)   # 派生类中访问
#
# obj = C()
#
# obj.__foo     # 通过对象访问    ==> 错误
# obj.func()  # 类内部访问        ==> 正确
#
# obj_son = D()
# obj_son.show()  # 派生类中访问  ==> 错误




