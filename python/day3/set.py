#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# old_dict = {
#     "#1": 8,
#     "#2": 4,
#     "#4": 2,
# }
#
# new_dict = {
#     "#1": 4,
#     "#2": 4,
#     "#3": 2,
# }
#
# # old_dict 中没有, new_dict 中有的加到 old_dict
#
# old_set = set(old_dict.keys())
# new_set = set(new_dict.keys())
#
# # print(old_set,new_set)
#
# remove_set = old_set.difference(new_set)
# add_set = new_set.difference(old_set)
# update_set = old_set.intersection(new_set)
#
# print("删除:%s\n添加:%s\n更新%s\n" % (remove_set, add_set, update_set))

# old_dict.pop(remove_set)
# old_dict[add_set] = new_set[add_set]
# for item in update_set:
#     old_dict[item] = new_dict[item]
#
# print(old_dict)


# 差集更新(在s中有的,在t中没有更新到s)
s = set("Hello")
t = set("World")

# print(s.union(t))  # s 和 t的并集(两个合并到一块)
# print(s | t)       #  简写
#
# print(s.intersection(t))  # s 和 t的交集(取出两个都有的)
# print(s & t)
#
# print(s.difference(t))  # 求差集(项在s中,但是不在t中)
# print(s - t)
#
# print(s.symmetric_difference(t)) # 对称差集(两个中不相同的)
# print(s ^ t)


# 集合aupdate方法添加多个元素,可以接受迭代的对象，循环add，批量添加
# add <-->update 的区别
# t = set("Hello")
# t.add("world")
# print(t)
# t1 = set("Hello")
# t1.update("world")
# print(t1)

# 集合discard方法,移除指定值,如果没有会报错
# s = set("Hello")
# s.discard("h")



