#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# def 发邮件():
#     import smtplib
#     from email.mime.text import MIMEText
#     from email.utils import formataddr
#
#     msg = MIMEText('邮件内容', 'plain', 'utf-8')
#     msg['From'] = formataddr(["武沛齐", 'wptawy@126.com'])
#     msg['To'] = formataddr(["走人", '424662508@qq.com'])
#     msg['Subject'] = "主题"
#
#     server = smtplib.SMTP("smtp.126.com", 25)
#     server.login("wptawy@126.com", "邮箱密码")
#     server.sendmail('wptawy@126.com', ['424662508@qq.com', ], msg.as_string())
#     server.quit()
#
# 发邮件()


# # 指定参数传递
# def send(A,B,C):
#     print(A,B,C)
#
#
# send(B="潘文斌", A="梁连", C="赵鸿飞")  # 要指定参数必须所有参数都要指定


# # 普通参数传递
# def send(A,B,C):
#     print(A,B,C)
#
#
# send("潘文斌", "梁连", "赵鸿飞")


# # 默认参数,没有传递参数,使用默认参数,传递了则使用传递的参数
# def send(A, B, C="SB"):
#     print(A, B, C)
#
# send("潘文斌", "梁连")


# # 非关键字可变长参数,可接收任意个参数
# def send(*args):
#     print(args)
#
# send("潘文斌", "梁连", "赵鸿飞")
# send(*["潘文斌", "梁连", "赵鸿飞"])   # 使用"*"可遍历序列,递归传參


# # 关键字可变长参数,也可接收任意个参数,参数传递形式:key-value
# def send(**kwargs):
#     print(kwargs)
#
# f1_dict = {
#     'a': 'aaa',
#     'b': 'bbb',
#     'c': 'ccc'
# }
#
# send(a='aaa', b='bbb', c='ccc')
# send(**f1_dict)


# 万能参数,可接收任意个参数,任意类型
# def send(*args, **kwargs):
#     print(*args)
#     print(*kwargs)
#
# send(1, 11, 21, k1='k1', k2='k2')


# # string的format()方法用到万能参数的例子
# s1 = "i am {0}, age {1}".format("lianglian", 12)
# print(s1)
#
# s2 = "i am {0}, age {1}".format(*["lianglian", 12])
# print(s2)
#
# s3 = "i am {name}, age {age}".format(name="lianglian", age=12)
# print(s3)
#
# dict={'name': 'liangian', 'age':12}
# s4 = "i am {name}, age {age}".format(**dict)
# print(s4)


# # python 函数多次定义被覆盖
# def f1(a1, a2):
#     return a1 + a2
#
# def f1(a1, a2):
#     return a1 * a2
#
# ret = f1(8,8)
# print(ret)


# # python 参数传递是引用
# def f1(a1):
#     a1.append(999)
#
# li = [11, 22, 33, 44]
# f1(li)
#
# print(li)


# # 函数内定义的变量只在该函数内有效(注意作用域)
# # global 修改全局变量
# NAME = 'alex'
#
# def f1():
#     age = 18
#     global NAME      # 使用global修改过全局变量,作用于全局
#     NAME = 'lianglian'
#     print(age, NAME)
#
# def f2():
#     age = 19
#     print(age, NAME)
#
# f1()
# f2()


# # 序列(list,tuple...) 行首定义的序列可以修改 但是不能重新赋值
# group = [11,22,33,44]
#
# def f1():
#     age = 18
#     group.append(55)
#     print(age, group)
#
# def f2():
#     age = 19
#     print(age, group)
#
# f1()
# f2()


# 三元运算  (简单的ifelse,只能写一行)
# name = "alex"
# name = "alex" if 1 == 2 else "SB"
# print(name)


# # lambda 表达式会自动retrun结果
# # lambda表达式  (简单的函数表达式,只能写一行)
# def f1(a1):
#     return a1 + 100
#
# ret = f1(10)
# print(ret)
#
# f2 = lambda a1: a1 + 100
#
# r2 = f2(10)
# print(r2)


# # 函数实參和形參之间是引用
# lists = [1, 2, 3, "q"]
# print(id(lists))     # 创建变量这个变量得时候的地址空间
# def name(li):
#     print(id(li))    # 引用实际参数,在这里内存地址空间还以一样
#
#     li = "c"
#     print(li)        # 只在这个函数内生效,就像是在这个函数内重新定义了一个"li"变量,和外面那个没关系
#     print(id(li))    # 这里是重新赋值了形参,所以地址空间变了
#
# name(lists)
# print(lists)
#
# # 函数内重新赋值作用域只限于函数内,函数内变了,外面没变
# name = "wu"
# def  show():
#     name='alex'
#     print(name)
# show()
# print(name)




# ######### 定义函数 #########
# 普通参数传递
# name 叫做函数send的形式参数，简称：形参
# def send(name):
#     print(name)

# ######### 调用函数 #########
#  "梁连" 叫做函数send的实际参数，简称：实参
# send("梁连")
