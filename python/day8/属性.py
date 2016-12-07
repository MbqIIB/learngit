#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# # ############### 定义 ###############
# class Foo:
#
#     def func(self):
#         pass
#
#     # 定义属性
#     @property
#     def prop(self):
#         pass
# # ############### 调用 ###############
# foo_obj = Foo()
#
# foo_obj.func()
# foo_obj.prop   #调用属性




# # ############### 定义 ###############
# class Pager:
#
#     def __init__(self, current_page):
#         # 用户当前请求的页码（第一页、第二页...）
#         self.current_page = current_page
#         # 每页默认显示10条数据
#         self.per_items = 10
#
#
#     @property
#     def start(self):
#         val = (self.current_page - 1) * self.per_items
#         return val
#
#     @property
#     def end(self):
#         val = self.current_page * self.per_items
#         return val
#
# # ############### 调用 ###############
#
# p = Pager(1)
# p.start    # 就是起始值，即：m
# p.end      # 就是结束值，即：n




# class Pager:
#
#     def __init__(self, all_count):
#         self.all_count = all_count
#
#     @property
#     def all_pager(self):
#         a1, a2 = divmod(self.all_count, 10)
#         if a2 == 0:
#             return a1
#         else:
#             return a1 + 1
#
#     @all_pager.setter
#     def all_pager(self, value):
#         self.all_count = value
#
#
#     @all_pager.deleter
#     def all_pager(self):
#         del self.all_count
#         print('del all_pager')
#
#
#
# p = Pager(101)
# ret = p.all_pager     # 仿字段一样操作,获取值
# print(ret)
#
# print(p.all_pager)
# p.all_pager = 121     # 仿字段一样操作,设置值
# print(p.all_pager)
#
# del p.all_pager       # 仿字段一样操作,删除值





# class Foo:
#
#     def get_bar(self):
#         return 'wupeiqi'
#
#     BAR = property(get_bar)
#
# obj = Foo()
# reuslt = obj.BAR        # 自动调用get_bar方法，并获取方法的返回值
# print(reuslt)




# class Foo:
#
#     def get_bar(self):
#         return 'wupeiqi'
#
#     # *必须两个参数
#     def set_bar(self, value):
#         return 'set value' + value
#
#     def del_bar(self):
#         return 'wupeiqi'
#     # property(fget=None, fset=None, fdel=None, doc=None)
#     BAR = property(get_bar, set_bar, del_bar, 'description...')
#
# obj = Foo()
#
# obj.BAR              # 自动调用第一个参数中定义的方法：get_bar
# obj.BAR = "alex"     # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
# del Foo.BAR          # 自动调用第三个参数中定义的方法：del_bar方法
# obj.BAR.__doc__     # 自动获取第四个参数中设置的值：description...


# class Goods(object):
#
#     def __init__(self):
#         # 原价
#         self.original_price = 100
#         # 折扣
#         self.discount = 0.8
#
#     def get_price(self):
#         # 实际价格 = 原价 * 折扣
#         new_price = self.original_price * self.discount
#         return new_price
#
#     def set_price(self, value):
#         self.original_price = value
#
#     def del_price(self):
#         del self.original_price
#
#     PRICE = property(get_price, set_price, del_price, '价格属性描述...')
#
# obj = Goods()
# obj.PRICE         # 获取商品价格
# obj.PRICE = 200   # 修改商品原价
# del obj.PRICE     # 删除商品原价









# class Pager:
#
#     def __init__(self, all_count):
#         self.all_count = all_count
#
#     def f1(self):
#         a1, a2 = divmod(self.all_count, 10)
#         if a2 == 0:
#             return a1
#         else:
#             return a1 + 1
#
#     def f2(self, value):
#         self.all_count = value
#
#
#     def f3(self):
#         del self.all_count
#         print('del all_pager')
#
#
#     foo = property(fget=f1,fset=f2,fdel=f3)
#
#
# p = Pager(110)
#
# result = p.foo
# print(result)
#
# p.foo = "alex"
#
# del p.foo




