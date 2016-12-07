#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import getpass
import os

# 判断一个用户连续登陆输错密码超过三次锁定用户

import json
import os
import getpass


def registered(user, password):
    '''
    用于用户注册
    :param user: 用户名
    :param password:  密码
    :return: 默认None 成功为True 失败为False
    '''
    confirm_password = input('请再次输入密码:')
    if os.path.getsize('./user.txt') == 0:
        with open('./user.txt', 'w') as dump_user_file:
            json.dump({'admin': {'lock': 0, 'password': 'admin', 'shop_car': {}, 'money': 0}}, dump_user_file)
    with open('./user.txt', 'r') as load_user_file:
        user_file_dict = json.load(load_user_file)
    if user in user_file_dict.keys():
        print('用户已经注册,不能反复注册!')
    elif password == confirm_password:
        user_dict = {
            user: {
                'password': password,
                'lock': 0,
                'shop_car': {},
                'money': 0
            }
        }
        with open('./user.txt', 'r') as load_user_file:
            json_user_dict = json.load(load_user_file)
        json_user_dict[user] = user_dict[user]
        with open('./user.txt', 'w') as dump_user_file:
            json.dump(json_user_dict, dump_user_file)
        print('恭喜您注册成功,您的用户名为%s' % user)
    else:
        print('您输入得密码不匹配')


def login(user, password):
    """
    用户用户登录
    :param user:
    :param password:
    :return:
    """
    with open('./user.txt', 'r') as user_file:
        user_dict = json.load(user_file)
    user_counter = 1
    flag = True
    while flag:
        # user_name = input("user:")
        # password = getpass.getpass("password:")
        # for user in user:   # 遍历从文件中读出来的字符串list
        #     user = user.strip().split()     # 遍历出来得字符串转化成list
        if user in user_dict.keys():  # 确认用户输入得用户名系统中存在
            if user_dict[user]['lock'] == 1:   # 判断是否是锁定用户
                print("您得用户已经被锁定,请联系管理员处理!")
                return False
            elif password == user_dict[user]['password']:
                print("%s 登录成功,欢迎您!" % user)
                return user
            else:
                print("用户名或密码错误!")
                while flag:
                    password = getpass.getpass("password:")
                    if password == user_dict[user]['password']:
                        print("%s 登录成功,欢迎您!" % user)
                        return user
                    print("用户名或密码错误!")
                    user_counter += 1
                    if user_counter >2:  # 输入错误2次以上
                        user_dict[user]['lock'] = 1   # 锁定用户
                        with open('./user.txt', 'w') as user_file:
                            json.dump(user_dict, user_file)
                        print("用户名或密码错误,输入错误3次,用户%s被锁定!" % user)
                        return False
        else:
            print('用户不存在!')
            return False


def modify_pwd(user, password):
    with open('./user.txt', 'r') as user_file:
        user_dict = json.load(user_file)
    if user_dict[user]['lock'] == 1:
        print('%s用户已被锁定,请联系管理解锁' % user)
    else:
        if user in user_dict.keys() and password == user_dict[user]['password']:
            new_password = getpass.getpass('请输入您新的密码:')
            user_dict[user]['password'] = new_password
            with open('./user.txt', 'w') as user_file:
                json.dump(user_dict, user_file)
                print('密码修改成功!')

        else:
            print('用户名或密码错误!')


def up_money(user, password):
    with open('./user.txt', 'r') as user_file:
        user_dict = json.load(user_file)
    if user in user_dict.keys() and password == user_dict[user]['password']:
        new_money = int(input('请输入您要充值得金额:'))
        user_dict[user]['money'] += new_money
        print('充值成功!您的当前金额为%d' % user_dict[user]['money'])
        with open('./user.txt', 'w') as user_file:
            json.dump(user_dict, user_file)
    else:
        print('用户名或密码错误!')


def shop_car(user, password):
    with open('./user.txt', 'r') as user_file:
        user_dict = json.load(user_file)
    if user in user_dict.keys() and password == user_dict[user]['password']:
        for product in user_dict[user]['shop_car']:
            print(product)
    else:
        print('用户名或密码错误!')


# user_name = input("user:")
# password = getpass.getpass("password:")
# # login(user_name,password)
# # modify_pwd(user_name, password)
# # up_money(user_name, password)
#
login_menu = '''
================================================
|               1.   登录系统                   |
|               2.   注册用户                   |
|               3.   修改密码                   |
|               4.   账户充值                   |
|               5.   退出                      |
================================================
'''

print(login_menu)
user_name = input("user:")
password = getpass.getpass("password:")
user_input = input('请输入您要做的操作序号:')
if user_input == '1':
    login(user_name, password)
elif user_input == '2':
    registered(user_name, password)
elif user_input == '3':
    modify_pwd(user_name, password)
elif user_input == '4':
    up_money(user_name, password)


