#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

print("Welcome to Liang’s shopping mall".center(50,'-'))

budget = int(input("请输入本次购物得预算(RMB):"))

product_list = [
    ("MacBook Air", 7999),
    ("Starbucks Coffee", 33),
    ("Iphone 6Plus", 6188),
    ("Python Booke", 60)
]

shop_car = []
flag = True
while flag:
    print("product list".center(50, '-'))
    for product in enumerate(product_list):
        p_id = product[0]
        p_name = product[1][0]
        p_price = product[1][1]
        print(p_id, '', p_name, p_price)
    user_input = input("[q=quit,c=check]请输入你想要购买的商品序号(0-%s):" % len(product_list)) # 把用户得输入调整到正确得list索引上
    if user_input.isdigit and int(user_input) < len(product_list):
        shop = product_list[int(user_input)]
        if budget >= shop[1]:
            shop_car.append(shop[0])
            budget -= shop[1]
            print("您已经成功购买: %s" % shop[0])
            print("您的预算:\033[41;1m[%s]\033[0m" % budget)
        else:
            print("当前预算不够购买此商品,请充值!")
    elif user_input == 'q' or user_input == 'quit':
        print("购物车".center(50, '*'))
        for shop_item in shop_car:
            print(shop_item)
        print("您的预算:\033[41:1m[%s]\033[0m" % budget)
        print("END".center(50, "*"))
    elif user_input == 'c' or user_input == 'check':
        print("购物车".center(50, '*'))
        for shop_item in shop_car:
            print(shop_item)
        print("您的预算:\033[41;1m[%s]\033[0m" % budget)
    # else:
    #     print("当前预算不够购买此商品,请联系管理员充值!")







