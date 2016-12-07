#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# import memcache
#
# mc = memcache.Client(['127.0.0.1:12000'], debug=True)
# mc.set("foo", "bar")
# ret = mc.get("foo")
#
# print(ret)


# import memcache
#
# # memcache 天生支持集群操作,权重觉得该借点请求操作次数
# host = [('127.0.0.1:12000', 1), ('192.168.0.1:12000', 2), ('192.168.0.2:12000', 3)]
# mc = memcache.Client(host)
#
# mc.set('k1', 'v1')
# ret = mc.get('k1')
# print(ret)


import memcache
mc = memcache.Client(['127.0.0.1:12000'], debug=True)
# add()方法添加健值对
# mc.add('k2', 'v2')
# ret = mc.add('k1', 'v1') # 报错! 对已经存在的key重复添加,失败!!!

# replace()方法修改某个key的值，如果key不存在，则异常
# mc.replace('k1', 11111)
# ret = mc.get('k1')
# print(ret)

# set            设置一个键值对，如果key不存在，则创建，如果key存在，则修改
# set_multi      设置多个键值对，如果key不存在，则创建，如果key存在，则修改
# mc.set('k3', 33333)
# mc.set_multi({'k1': 111, 'k2': 222, 'k3': 333})
# ret = mc.get('k1')
# print(ret)

# delete             在Memcached中删除指定的一个键值对
# delete_multi       在Memcached中删除指定的多个键值对
# mc.delete('k1')
# mc.delete_multi(['k1', 'k2', 'k3'])

# get            获取一个键值对
# get_multi      获取多一个键值对
# ret1 = mc.get('k1')
# ret2 = mc.get_multi(['k1', 'k2', 'k3'])


# append    修改指定key的值，在该值 后面 追加内容
# prepend   修改指定key的值，在该值 前面 插入内容
mc.append('k1', 222)
ret = mc.get('k1')
print(ret)