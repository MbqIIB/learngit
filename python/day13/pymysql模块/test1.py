#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# import pymysql
# # 创建连接
# connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123123', db='test')
# # 创建游标
# cursor = connection.cursor()
#
# # 执行SQL,并返回受影响行数
# effect_row = cursor.execute("update host set ip = '1.1.1.1'")
#
# # 执行SQL,并返回受影响行数
# effect_row = cursor.execute("update host set ip = '2.2.2.2' where hostname = 'c2'")
#
# # 执行SQL,插入多行数据并返回受影响行数
# effect_row = cursor.executemany("insert into host(hostname,port,ip)value(%s,%s,%s)", [("c6", 22, "6.6.6.6"), ("c7", 22, "7.7.7.7")])
# print(effect_row)
# # 提交,不然无法保存修改
# connection.commit()
#
# # 关闭游标
# cursor.close()
# # 关闭连接
# connection.close()



import pymysql
# 创建连接
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123123', db='test')
# 创建游标
cursor = connection.cursor()

cursor.execute("select * from host")

# # 获取第一行数据
# row = cursor.fetchone()
# print(row)

# # 正数向下移动指针
# cursor.scroll(1, mode='relative')
# row_3 = cursor.fetchone()
# print(row_3)

# 负数向上移动指针
cursor.scroll(7, mode='absolute')
row_1 = cursor.fetchone()
print(row_1)

# 提交,不然无法保存修改
connection.commit()
# 关闭游标
cursor.close()
# 关闭连接
connection.close()




# import pymysql
# # 创建连接
# connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123123', db='test')
# # 创建游标,设置为字典类型
# cursor = connection.cursor(cursor=pymysql.cursors.DictCursor)
#
# cursor.execute("select * from host")
#
# # 获取第一行数据
# row = cursor.fetchone()
# print(row)
#
# # 提交,不然无法保存修改
# connection.commit()
# # 关闭游标
# cursor.close()
# # 关闭连接
# connection.close()





