#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# class Foo:
#
#     __cc = "123"
#
#     def __init__(self, name):
#         self.__name = name
#
#     def f1(self):
#         print(self.__name)
#
#
#     @staticmethod
#     def f3():
#         print(Foo.__cc)


# obj = Foo('alex')
# obj.f1()
# Foo.f3()



# class Foo:
#
#     def __init__(self, name):
#         self.__name = name
#
#     def f1(self):
#         print(self.__name)
#
# class Bar(Foo):
#
#     def f2(self):
#         print(self.__name)
#
#
# obj = Bar('alex')
# # obj.f2()
# obj.f1()



class Foo:

    def __init__(self, name):
        self.__name = name

    def __pav(self):
        print(self.__name)

    def pul(self):
        self.__pav()

obj = Foo('alex')
# obj.__pav()
obj.pul()

print(obj._Foo__name)#  强制访问私有属性