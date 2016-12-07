#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import json
import os
import getpass
import time

from user import *


def shoping():
    print("梁先森万能商店**只有你想不到,没有这里买不到".center(50, '*'))   # 运行程序,打印欢迎语

    user_name = input("user:")
    password = getpass.getpass("password:")

    user_retrun = login(user_name, password)   # login函数 登录成功才会retrun user_name
    if user_retrun != 1:     # 登录是否成功了,异常user_retrun 为1
        flag = True
        while flag:
            print("万能商店分类".center(51, '='))
            shop_dir = os.listdir('./product/')   # 得到商店主目录下目录,返回list
            for index, shop in enumerate(shop_dir):
                print('|', '%s.%s'.center(48, ) %(index, shop), '|')    # 目录以菜单得形式打印出来
            print('='.center(55, '='))
            shop_input = input("[q=退出,c=查看]请输入菜单序号(0-%s):" % len(shop_dir))
            if shop_input.isdigit() and int(shop_input) < len(shop_dir):
                shop_input = int(shop_input)
                with open('./product/%s/product.txt' % shop_dir[shop_input], 'r', encoding='utf-8') as shop_file:
                    for product_index, product_list in enumerate(shop_file.readlines()):
                        product_list = product_list.split()    # 每行转换成list处理
                        product_item = product_list[0]
                        product_price = product_list[1]
                        print('%s.%s\t%s' % (product_index, product_item, product_price))
                with open('./product/%s/product.txt' % shop_dir[shop_input], 'r', encoding='utf-8') as shop_file:
                    product_num = len(shop_file.readlines())
                product_input = input("[q=退出,c=查看]请输入菜单序号:")
                if product_input.isdigit() and int(product_input) < product_num:
                    product_input = int(product_input)
                    with open('./product/%s/product.txt' % shop_dir[shop_input], 'r', encoding='utf-8') as shop_file:
                        shop_list = shop_file.readlines()
                    user_product_list = shop_list[product_input].split()   # 从整个shop文件中读出所有用户选择的product,去空行,转list
                    with open('./user.txt', 'r', encoding='utf-8') as user_file:
                        user_dict = json.load(user_file)
                    if user_dict[user_name]['money'] > int(user_product_list[1]):
                        user_product = user_product_list[0]
                        if user_product in user_dict[user_name]['shop_car'].keys():
                            user_dict[user_name]['shop_car'][user_product]['number'] += 1
                            user_dict[user_name]['shop_car'][user_product]['price'] += user_product_list[1]
                            user_dict[user_name]['shop_car'][user_product]['time'] = time.strftime("%Y-%m-%d %H:%M:%S")
                            user_dict[user_name]['money'] -= int(user_product_list[1])
                            with open('./user.txt', 'w', encoding='utf-8') as user_file:
                                user_dict = json.dump(user_dict, user_file)
                            print("您当前余额为%s" % user_dict[user_name]['money'])
                        else:
                            user_dict[user_name]['shop_car'][user_product] = {
                                'number': 1,
                                'price': user_product_list[1],
                                'time': time.strftime("%Y-%m-%d %H:%M:%S")
                            }
                            user_dict[user_name]['money'] -= int(user_product_list[1])
                            with open('./user.txt', 'w', encoding='utf-8') as user_file:
                                user_dict = json.dump(user_dict, user_file)
                                print("您当前余额为%s" % user_dict[user_name]['money'])
                    else:
                        print("您当前余额不够购买此商品!")
                elif product_input == 'q':
                    flag = False
                    print('谢谢惠顾,下次再来~')

                elif product_input == 'c':
                    with open('./user.txt', 'r', encoding='utf-8') as user_file:
                        user_dict = json.load(user_file)
                    print("购物清单".center(100, '='))
                    print("|       prodct           number            price            time               |")
                    for user_product in user_dict[user_name]['shop_car'].keys():
                        print("prodct    number    price    time")
                        number = user_dict[user_name]['shop_car'][user_product]['number']
                        price = user_dict[user_name]['shop_car'][user_product]['price']
                        date = user_dict[user_name]['shop_car'][user_product]['time']
                        print("%s    %s    %s    %s" % (user_product, number, price, date))
                    print("您当前余额为[%s]" % user_dict[user_name]['money'])

            elif shop_input == 'q':
                flag = False
                print('谢谢惠顾,下次再来~')

            elif shop_input == 'c':
                with open('./user.txt', 'r', encoding='utf-8') as user_file:
                    user_dict = json.load(user_file)
                print("购物车清单".center(50, '='))
                print('      prodct         number        price         time        ')
                for user_product in user_dict[user_name]['shop_car'].keys():
                    number = user_dict[user_name]['shop_car'][user_product]['number']
                    price = user_dict[user_name]['shop_car'][user_product]['price']
                    date = user_dict[user_name]['shop_car'][user_product]['time']
                    print('       %s                  %s             %s          %s         ' % (user_product, number, price, date))
                print('====='.center(45, '='), "您当前余额为[%s]" % user_dict[user_name]['money'])

login_menu = '''
==========================================
|             1.   登录系统              |
|             2.   注册用户              |
|             3.   修改密码              |
|             4.   账户充值              |
=========================================
'''

print(login_menu)

user_input = input('请输入您要做的操作序号:')
if user_input == '1':
    shoping()
elif user_input == '2':
    user = input("user:")
    password = getpass.getpass("password:")
    registered(user, password)
elif user_input == '3':
    user = input("user:")
    password = getpass.getpass("password:")
    modify_pwd(user, password)
elif user_input == '4':
    user = input("user:")
    password = getpass.getpass("password:")
    up_money(user, password)
