#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 通过字典的update方法拿一个新的字典去更新一个旧的字典
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT"
# }
#
# test_dict = {
#     'name': 'liang',
#     'address': 'BeiJin'
# }
# user_info.update(test_dict)  #
# print(user_info)


# 字典的setdefault方法可以安全得去修改一个key得值,这个key存在不会覆盖掉
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT"
# }
#
# print(user_info.setdefault('name','Test'))
# print(user_info)
# 找一个key为'name'的记录,如果这个key不存在,那就创建一个叫'name'的key,
# 并且将其value设置为'Test',如果这个key存在,就直接返回这个key的value


# 字典的pop方法删除指定一条数据
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT"
# }
#
# user_info.pop('name')  # 删除'name'这条数据
# print(user_info)


# 字典的get方法安全的去查询一个key得value,不存在得key不会报错
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT"
# }
#
# print(user_info.get('na'))  # 查找一个key,如果存在则返回value,如果不存在不会报错,返回None


# 字典的keys方法可以将字典的key以字典视图的形式返回(相对上面两种推荐使用这种,通过key去取value)
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT"
# }
#
# print(user_info.keys())  # 将dict的key转换成字典视图形式的list，再通过list函数转换成真正可操作的list
# print(list(user_info.keys()))


# 字典的popitem方法会随机删除一条字典得数据(尽量不要使用)
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT"
# }
#
# user_info.popitem()  # 随机删除一条数据,dict为空得时候会报错
# print(user_info)


# 字典的copy模块的deepcopy方法实现深copy
# import copy
# user_info = {
#     "name": "lianglian",
#     "age": 12,
#     "job": "IT",
#     "hobby": {
#         "book": "三国演义",
#         "movement": "skateboard"
#     }
# }
#
# new_user_info = copy.deepcopy(user_info)
# print(user_info)
# print(new_user_info)
# user_info['age'] = 16
# user_info['hobby']['book'] = '三体'
# print(user_info)
# print(new_user_info)


# fi.e = open('./txt', 'r')
# print(fi.e)

# with open('./txt', 'r') as f.e:
#     print(f.e)


# 遍历dict
user_info = {
    "name": "lianglian",
    "age": 12,
    "job": "IT"
}

for item in user_info:
    print(item, user_info[item])