#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian
# python 内置函数

# 内置函数abs()取绝对值
# print(abs(-10))

# bool() 求布尔值
# print(bool(1))
# print(bool(None))
#
# all()所有为真,结果才为真
# print(all([1, 2, 3, None]))
#
# any()只要有真,结果就为真
# print(any([[], 0, "", 1]))
#
# # ascii() # 自动执行对象的 __repr__方法
#
# # bin() 转换2进制  0b
# print(bin(10))
#
# # oct() 转换8进制  0o
# print(oct(10))
#
# # hex() 转换16进制 0x
# print(hex(10))
#
#
# # bytes()字符转换成字节
# s = "梁"
# n = bytes(s, encoding="utf-8")
# # n = bytes(s, encoding="gbk")
# print(n)
#
#
# str()字节转换字符串
# s = "梁"
# n = bytes(s, encoding="utf-8")
# print(n)
# new_str = str(n, encoding="utf-8")
# print(new_str)


# 打开文件,加b就是二进制操作(b读得方式用二进制读和写容易出问题)
# f = open('./txt', 'r')   # 只读
# f = open('./txt', 'rb')  # 二进制打开,返回二进制格式,无python处理字节
# f = open('./txt', 'wb')  # 二进制写入,无python处理字节
# f = open('./txt', 'w')   # 只写,如果文件存在会清空
# f = open('./txt', 'x')   # 只写,py3新增,文件存在报错,
# f = open('./txt', 'a')   # 尾行追加
# f = open('./txt', 'a', encoding="utf-8")  # 指定编码打开文件
#
#
# # 指定编码打开文件,加b得话读取按照字节方式
# f = open('./txt', 'r+', encoding="utf-8")  # 指定编码打开文件,加b得话读取按照字节方式
# f.read(1)  # 无参数读全部,读取第一个字符(+b 读取第一个字节)
# f.seek(1)  # 移动当前指针位置(字符,和打开方式没有关系,不影响)
# f.tell()   # 获取当前指针位置(字符,和打开方式没有关系,不影响)
# f.write("11")  # 当前指针位置向后写(向后覆盖,打开方式有b字节,无b字符)
#
# f.close()  # 关闭文件
# f.flush()   # 刷新文件缓冲区到硬盘
# f.readable()  # 判断是否可读
# f.truncate()  # 截断, 文件可操作,从指针位置后面清空
# #
# # with 最后会close
# with open('./txt', 'r') as file:
#     file.read()


# f = open('./txt', 'r+', encoding="utf-8")
# data = f.read(3)
# f.seek(f.tell())
# f.write("A")
# f.close()
#
#



# # # py3 新功能
# with open('./txt', 'r', encoding="utf-8") as f1, open('./txt', 'w', encoding="utf-8") as f2:
#     times = 0
#     for line in f1:
#         times += 1
#         if times <= 10:
#             f2.write(line)
#         else:
#             break





