#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import getpass
import os


def registered():
    """
    注册用户
    :return:
    """
    user_name = input("请输入用户名:")
    password = input("请输入密码:")
    confirm_password = input("请再次输入密码:")
    if password == confirm_password:
        mail = input("请输入用户邮箱:")
        phone = input("请输入用户手机号:")
        with open("./user_info", 'a') as user_info_file:
            user_info = [user_name, password, mail, phone, '0']
            user_info = "|".join(user_info)
            user_info_file.write("%s\n" % user_info)
    else:
        print("您两次输入密码不匹配!")


def update_password(user_name):
    """
    修改用户密码
    :param user_name: 用户名
    :return: True 修改密码成功
    """
    new_password = input("请输入您需要设置的新密码:")
    confirm_password = input("请再次输入您设置的新密码:")
    if new_password == confirm_password:
        with open("./user_info", 'r') as user_info_file, open("./user_info.tmp", 'w') as user_info_tmp:
            for user_info in user_info_file:
                user_info = user_info.split("|")
                if user_name == user_info[0]:
                    user_info[1] = new_password
                user_info = "|".join(user_info)
                user_info_tmp.write(user_info)
            os.rename("./user_info.tmp", "./user_info")
            print("密码修改成功!")
            return True


def scan_user_info(user_name):
    """
    查看当前用户信息
    :param user_name: 用户名
    :return:
    """
    with open("./user_info", 'r') as user_info_file:
        for user_info in user_info_file:
            user_info = user_info.strip().split("|")
            if user_name == user_info[0]:
                print("用户名   密码    邮箱            手机号   特权")
                print("\t".join(user_info))


def search_user_info():
    """
    关键字搜索用户信息
    :return:
    """
    keyword = input("请输入用户信息关键字:")
    with open("./user_info", 'r') as user_info_file:
        print("用户信息搜索".center(50, "="))
        for user_info in user_info_file:
            user_info = user_info.strip().split("|")
            for user in user_info:
                if keyword in user:
                    print("|".join(user_info))


def update_user_info():
    """
    修改过用户信息
    :return:
    """
    menu = """
            ============用户信息修改==============
            |           1.修改用户密码           |
            |           2.修改用户邮箱           |
            |           3.修改用户手机号         |
            |           4.修改用户权限           |
            |           5.返回上一层            |
            ===================================
            """
    while True:
        with open("./user_info", 'r') as user_info_file, open("./user_info.tmp", 'w') as user_info_tmp:
            print(menu)
            menu_input = input("\033[33;0m您所需要做的操作:\033[0m")
            if menu_input == '1':
                user = input("请输入要操作的用户名:")
                update_password(user)
            elif menu_input == '2':
                user = input("请输入要操作的用户名:")
                new_mail = input("请输入新的内容:")
                for user_info in user_info_file:
                    user_info = user_info.strip().split("|")
                    if user == user_info[0]:
                        user_info[2] = new_mail
                    user_info = "|".join(user_info)
                    user_info_tmp.write("%s\n" % user_info)
                os.rename("./user_info.tmp", "./user_info")
            elif menu_input == '3':
                user = input("请输入要操作的用户名:")
                new_phone = input("请输入新的内容:")
                for user_info in user_info_file:
                    user_info = user_info.strip().split("|")
                    if user == user_info[0]:
                        user_info[3] = new_phone
                    user_info = "|".join(user_info)
                    user_info_tmp.write("%s\n" % user_info)
                os.rename("./user_info.tmp", "./user_info")
            elif menu_input == '4':
                user = input("请输入要操作的用户名:")
                new_permissions = input("请输入新的内容(0|1):")
                if new_permissions == '0' or new_permissions == '1':
                    for user_info in user_info_file:
                        user_info = user_info.strip().split("|")
                        if user == user_info[0]:
                            user_info[4] = new_permissions
                        user_info = "|".join(user_info)
                        user_info_tmp.write("%s\n" % user_info)
                    os.rename("./user_info.tmp", "./user_info")
                else:
                    print("输入有误,请按照提示输入!")
                    continue
            elif menu_input == '5':
                return
            else:
                print("您的输入有误,请重新输入")


def validation(func):
    """
    装饰器区分用户
    :param func: 原登录函数
    :return: 新的原登录函数
    """
    def check():
        user_menu = """\033[36;0m
        ============普通用户操作==============
        |           1.修改密码              |
        |           2.查看资料              |
        |           3.注销                 |
        ===================================
        \033[0m"""
        admin_menu = """\033[36;0m
        =============管理员操作==============
        |           1.修改密码              |
        |           2.添加用户              |
        |           3.修改用户信息           |
        |           4.查看用户信息           |
        |           5.搜索用户信息           |
        |           6.注销                 |
        ===================================
        \033[0m"""
        ret = func()
        with open("./user_info", "r") as user_info_file:
            for user_info in user_info_file:
                user_info = user_info.strip().split("|")
                if ret == user_info[0] and user_info[4] == '1':
                    while True:
                        print(admin_menu)
                        menu_input = input("\033[33;0m您所需要做的操作:\033[0m")
                        if menu_input == '1':
                            update_password(user_name)
                        elif menu_input == '2':
                            registered()
                        elif menu_input == '3':
                            update_user_info()
                        elif menu_input == '4':
                            scan_user_info(user_name)
                        elif menu_input == '5':
                            search_user_info()
                        elif menu_input == '6':
                            break
                        else:
                            print("您的输入有误,请重新输入")
                elif ret == user_info[0] and user_info[4] == '0':
                    while True:
                        print(user_menu)
                        menu_input = input("\033[33;0m您所需要做的操作:\033[0m")
                        if menu_input == '1':
                            update_password(user_name)
                        elif menu_input == '2':
                            scan_user_info(user_name)
                        elif menu_input == '3':
                            break
                        else:
                            print("您的输入有误,请重新输入")

    return check


@validation
def login():
    """
    用户登录
    :return:  登录成功用户名
    """
    user_name = input("input your user name:")
    password = input("input your password:")

    global user_name
    with open("./user_info", 'r', encoding="utf-8") as user_info_file:
        for user_info in user_info_file:
            user_info = user_info.strip().split("|")
            if user_name == user_info[0] and password == user_info[1]:
                print("欢迎你:\033[32;0m[%s]\033[0m 登录成功!" % user_name)
                return user_name
        print("用户或密码错误")
        return False


menu = """\033[36;0m
============用户管理系统==============
|           1.登录系统              |
|           2.注册用户              |
|           3.退出                 |
===================================
\033[0m"""

while True:
    print(menu)
    menu_input = input("\033[33;0m您所需要做的操作:\033[0m")
    if menu_input == '1':
        login()
    elif menu_input == '2':
        registered()
    elif menu_input == '3':
        break
    else:
        print("您的输入有误,请重新输入")

