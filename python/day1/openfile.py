#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# f = open('/Users/lianliang/PycharmProjects/python_-study/day1/user.txt', 'r')  # 使用Python内置的open()函数以读'r'文件的模式打开一个文件对象,读完了就没了,要赋值给变量
# print(f.read())        # 通过read()方法可以可以一次读取文件的全部内容
# f.close()



# with open('/Users/lianliang/PycharmProjects/python_-study/day1/user.txt', 'r') as f:  # 放在with里面 with最后会调用close() 不用我们再写close
#     for line in f.readlines():
#         print(line)


'''
# 创建一个新文件,如果有这个文件,会被覆盖
f = open('/Users/lianliang/PycharmProjects/python_-study/day1/user.txt', 'w')
f.write('aaa\t111\n')
f.close()
'''

'''
# 在现有文件后面追加内容
f = open('/Users/lianliang/PycharmProjects/python_-study/day1/user.txt', 'a')
f.write('aaa\t222\n')
f.close()
'''


# 在原有文件上修改
f = open('./user.txt', 'r')
new_f = open('./user1.txt', 'w')
for line in f.readlines():
    if 'lianglian' in line:
        line = line.replace('0', '1')
    new_f.write(line)
f.close()
new_f.close()
import os
os.rename('./user1.txt', './user.txt')  # 新文件覆盖旧文件




