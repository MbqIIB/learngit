#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian



# 判断用户登陆
# user = 'liang'
# passwd = 'liang'
#
# username = input("username:")
# password = input("password:")
#
# if  user == username and passwd == password:
#     print("Welcome login...")
# else:
#     print("username or password is error!")






# 猜年龄
# age = 12
# for i in range(10):
#     if i < 3:
#         guess_num = int(input("input your guess num:"))
#         if guess_num == age:
#             print("猜对了,恭喜!")
#             break    # 跳出整个循环
#         elif guess_num > age:
#             print("大了!")
#         else:
#             print("小了!")
#     else:
#         print("尝试次数太多!")
#         break



# 猜年龄
age = 22
counter = 0
for i in range(10):
    if counter < 3:
        guess_num = int(input("input your guess num:"))
        if guess_num == age:
            print("猜对了,恭喜!")
            break  # 跳出整个循环
        elif guess_num > age:
            print("大了!")
        elif guess_num < age:
            print("小了!")
    else:
        contionue_confirm = input("是否继续(y/n):")
        if contionue_confirm == 'y':
            counter = 0
            continue  # 跳出单次循环
        else:
            print("拜拜!")
            break

    counter += 1
