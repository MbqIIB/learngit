#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import getpass
import os

# 判断一个用户连续登陆输错密码超过三次锁定用户

txt = open('./user.txt', 'r')
new_txt = open('./user1.txt', 'w')
users = txt.readlines()  # 返回文件的list字符串格式,赋值给变量,因为读文件只能读一次,无法多次使用(遇到的坑)
user_counter = 1
flag = True
while flag:
    user_name = input("user:")
    password = getpass.getpass("password:")
    for user in users:   # 遍历从文件中读出来的字符串list
        user = user.strip().split()     # 遍历出来得字符串转化成list
        if user_name in user:  # 确认用户输入得用户名系统中存在
            if user[2] == '1':   # 判断是否是锁定用户
                print("您得用户已经被锁定,请联系管理员处理!")
                flag = False
                break
            elif user_name == user[0] and password == user[1]:
                print("%s 登录成功,欢迎您!" % user_name)
                flag = False
                break
            elif user_counter > 2:  # 输入错误2次以上
                for lock in users:     # 遍历原文件内容
                    if user_name in lock:  # 匹配到要修改的那行内容
                        lock = lock.replace('0', '1')   # 修改内容并重新赋值
                    new_txt.write(lock)   # 遍历原文件和修改得内容写到新的文件中
                txt.close()
                new_txt.close()
                os.rename('./user1.txt', './user.txt')  # 新文件覆盖旧文件,达到修改原文件得效果
                print("用户名或密码错误,输入错误3次,用户%s被锁定!" % user_name)
                flag = False
                break
            else:
                user_counter += 1
                print("用户名或密码错误!")
                break



