#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# 用户输入
# user_name = input("input your name:")
# user_age = input("input your age:")
# user_jobe = input("input your jobe:")
#
#
# print("user input name:",user_name)
# print("user input age:",user_age)
# print("user input work:",user_jobe)






# 文本格式化
# user_name = input("input your name:")
# user_age = input("input your age:")
# user_jobe = input("input your jobe:")
#
# msg = """
# Infomation of user %s:
# -------------------
# Name:   %s
# Age :   %s
# Job :   %s
# ---------End-------
# """
#
# print(msg % (user_name, user_name, user_age, user_jobe))



# 密文输入
# import getpass
#
# name = input("Please input your name:")
# password = getpass.getpass("Please input your password:")
#
# print("your name is:%s\npassword is:%s" % (name, password))


# print("\033[1;30;42mHello World!\033[0m", "\033[1;30;47mHello World!\033[0m")
# print("\033[1;31;42mHello World!\033[0m", "\033[1;30;41mHello World!\033[0m")
# print("\033[1;37;42mHello World!\033[0m", "\033[1;30;42mHello World!\033[0m")
# print("\033[1;33;42mHello World!\033[0m", "\033[1;30;43mHello World!\033[0m")
# print("\033[1;34;42mHello World!\033[0m", "\033[1;30;44mHello World!\033[0m")
# print("\033[1;35;42mHello World!\033[0m", "\033[1;30;45mHello World!\033[0m")
# print("\033[1;36;42mHello World!\033[0m", "\033[1;30;46mHello World!\033[0m")




# your_name = input("What's your name:")
# print("Hello ,%s!" % your_name)



# 字符串isdigt方法来判断字符串是不是数字
# s = "liang lian"
# print(len(s))
# print(s)
# s1 = s.lower()
# print(len(s1))
# print(s1)

# s1 = "45"
# print(s1.isdigit())


# 字符串endswith方法判断字符串是以什么结尾的
s = "liang lian"
# print(s.endswith("n"))

# 万恶得“＋”号
# print("a" + "b" + "c") # 会开辟三块地址空间，

# list函数将对象转换成列表
# l = (1,2,3,4)
# l.index()
# print(type(l))


# 创建元组
# t = (1, 2, 3, "lianglian")
# print(t)
#
# t1 = tuple([1, 2, 3, "lianlgian"])  # 数据类型转换
# print(t1)
#
# print(len(t))  # 计算元组中有多少个元素

# t1 = t + (4,5,6)
# print(t2)

# 元组分片[起始位:结束位:步长]
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, (1,2,3))
# print(t[0])      # []中输入索引进行分片,索引起始位为0
# print(t[3:6])    # 显示4~6得元素
# print(t[3:])     # 显示4到最后
# print(t[:6])     # 显示从开头到7
# print(t[-1])     # 显示倒数第一个
# print(t[-4:-2])  # 显示倒数第4个到倒数第二个,(**范围切片,结束位不包括在内,即"到什么什么之前"**)
# print(t[:])      # 显示全部
# print(t[::2])    # 按照步长为2,显示全部,**步长即两个元素之间索引闲差多少执行一次**
# print(t[9][0])   # 嵌套分片

# # 创建元组
# t = (1, 2, 3, "lianglian")
# print(t)
#
# t1 = tuple([1, 2, 3, "lianlgian"])  # tuple将其它序列转换成元组
# print(t1)
#
# t2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, (1, 2, 3))  # 创建嵌套元组
#
# print(t * 3)   # 元组复制
#
# t3 = t + t2    # 元组合并
# print(t3)


# 查看元素在元组中得数量
t = (1, 2, 3, "lianglian", 3,)
# print(t.count(3))

list
