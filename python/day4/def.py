#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 函数没有return返回值,默认返回None
# li = [11, 22, 33, 44,]
#
#
# def f1(arg):
#     arg.append(55)
#
# # li = f1(li)
# f1(li)
# print(li)


# # ascii 转换
# r = chr(65)  # 输入数字返回ascii中对应的的字符
# print(r)
#
# s = ord('A')  # 输入字符返回ascii中对应位置
# print(s)

# 生成随机码
# import random
# li = []
# for i in range(11):
#     r = random.randrange(0, 5)
#     if r == 2 or r == 4:
#         item = random.randrange(0, 10)
#         li.append(str(item))
#     else:
#         item = random.randrange(65, 91)
#         c = chr(item)
#         li.append(c)
#
# result = "".join(li)
# print(result)



# # compile() # 编译, single,eval,exec
# # 将字符串编译成python代码,= sring or file
# s = "print(123)"
# r = compile(s, "<string>", "exec")
# #执行代码,接收代码和字符串都能执行,没有返回值
# print(r)
# ret = exec(r)  # exec() 执行python的代码
#
# # eval()执行表达式,并返回结果
# s = "8*8"
# ret = eval(s)
# print(ret)


# # 快速查看类为对象提供了哪些功能
# print(dir(list))
#
# # 查看源码帮助信息
# help(list)

# divmod()求商和余数
# r = divmod(97, 10)
# print(r)


# # isinstance()判断对象,对象是否是某个类的实例
# s = [1,2,3,22]
# r = isinstance(s, list)
# print(r)

# # filter() 过滤条件
# # filter # 函数返回True,将元素添加到结果中
# # filter(函数,可迭代的对象)
# # filter内部迭代第二个参数
# # result = []
# # for item in 第二个参数:
# #     r = 第一个参数(item)
# #     if r :
# #         result.append(item)
# # return result
# # filter ,循环第二个参数,让每个循环元素执行函数,如果函数返回True,表示元素合法
def f2(num):
    if num > 22:
        return True

li = [11, 22, 33, 44, 55, ]

ret = filter(f2, li)
print(list(ret))
#
# # 简写
# li = [11, 22, 33, 44, 55]
# result = filter(lambda num: num > 33, li)
# print(list(result))



# # map()  迭代操作
# # map()  # 将函数retrun,放到结果中
# li = [11, 22, 33, 44, 55]
#
# # map(函数,可迭代的对象(可以for循环的东西))
# def f2(a):
#     return a + 100
#
# result = map(f2, li)
# print(list(result))

# 简写
# result = map(lambda a: a + 100, li)



# locals()   # 代表所有局部变量
# globals()  # 代表所有全局变量


# # len()取字符串和子节长度,在python3中len()取的是字符的长度
# s = "梁连"
# print(len(s))
#
# b = bytes(s, encoding='utf-8')
# print(len(b))

# <林达看美国>


# json.logds() 将一个字符串,转换成python基本数据类型.

# {"k1":"v1"} 字典如果想要通过json转换成python字典类型,内部得字符串必须是双引号"

# # max() min() sum() 分别求最大,最小,求和.
# print(max([11,22,33]))
# print(min([11,22,33]))
# print(sum([11,22,33]))

# print(2**10)
# print(pow(2, 10))  # 幂运算

# reversed() 方法反转序列
# l = [11, 22, 33, 44]
# print(list(reversed(l)))  # 反转,和list的reverse方法一样
# print(list(reversed("liang")))
# l.reverse()
# print(l)

# # 四舍五入
# print(round(1.8))

#
# # sorted()  # 排序
# l = [3,2,1,4,5,6,9,]
# l1 = sorted(l)
# print(l1)

#
# # zip() # 拉链,交叉,不相等长不互补,多余的丢弃
# l = [11, 22, 33, ]
# l1 = ['aa', 'bb', 'cc', 'dd', 'ee', ]
# print(list(zip(l, l1)))

