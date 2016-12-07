#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# class Province:
#     country = "中国"
#
#     def __init__(self, name):
#         self.name = name
#     # 普通方法,由对象去调用执行(方法属于类 )
#
#
#     @staticmethod
#     def f1(arg1, arg2):
#         # 静态方法,由类调用执行
#         print(arg1, arg2)
#
#     @classmethod
#     def f2(cls):
#         obj = cls('河南')
#         print(cls, obj.name, cls.country)
#
#
# Province.f1(111,222)
# Province.f2()




class Foo:

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """

        print('普通方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """

        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""

        print('静态方法')



# 调用普通方法
f = Foo()
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()