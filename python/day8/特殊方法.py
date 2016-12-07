#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# class Foo:
#
#     # 构造方法
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     # 析构方法
#     def __del__(self):
#         print("class end!")
#
#
#     # 对象()
#     def __call__(self,):
#         print('call')
#
#     # 直接执行对象,print会方法对象内存地址,str方法返回更友好方式
#     def __str__(self):
#         return "%s - %d" % (self.name, self.age)
#
#     def __getitem__(self, item):
#         # print(type(item))
#         print(item)
#
#     def __setitem__(self, key, value):
#         # print(type(key), type(value))
#         print("{%s:%s}" % (key, value))
#
#     def __delitem__(self, key):
#         # print(type(key))
#         print('del %s' % key)
#
#
# # obj = Foo('alex', 66)
# # obj() # 对象() 执行call方法
# # # Foo()()
# #
# # obj1 = Foo('alex', 73)
# # obj2 = Foo('eric', 84)
# #
# # # 直接执行对象,print会方法对象内存地址,str方法返回更友好方式
# # print(obj1)
# # print(obj2)
# #
# # __dict__ 字典形式返回字对象所有的方法
# # ret = obj1.__dict__
# #
# # print(ret)
#
#
# obj = Foo('alex', 66)
# obj[1:4:2]
# obj[1:4] = [11,22,33,44,55]
# del obj[1:4]




# class Foo:
#
#
#     # 被for(迭代器迭代),执行这个方法的__iter__方法
#     def __iter__(self):
#         yield 1
#         yield 2
#         yield 3
#         yield 4
#
# obj = Foo()
#
# for item in obj:
#     print(item)




# class MyType(type):
#
#     def __init__(self, what, bases=None, dict=None):
#         super(MyType, self).__init__(what, bases, dict)
#
#     def __call__(self, *args, **kwargs):
#         obj = self.__new__(self, *args, **kwargs)
#
#         self.__init__(obj)
#
# class Foo(object):
#
#     __metaclass__ = MyType
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls, *args, **kwargs)
#
# # 第一阶段：解释器从上到下执行代码创建Foo类
# # 第二阶段：通过Foo类创建obj对象
# obj = Foo()



# class Foo(object):
#     pass
#
# obj = Foo()
#
# # 检查是否obj是否是类 cls 的对象
# print(isinstance(obj, Foo))



# class Foo(object):
#     pass
#
# class Bar(Foo):
#     pass
#
# # 检查Bar类是否是 Foo 类的派生类
# print(issubclass(Bar, Foo))





# while True:
#     num1 = input('num1:')
#     num2 = input('num2:')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         result = num1 + num2
#     except Exception as e:
#         print('出现异常，信息如下：')
#         print(e)





