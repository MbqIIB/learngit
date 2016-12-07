#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import os
import datetime
import json
import getpass

# 加载配置文件
from etc import config
from lib import commons
from src.log import debug_log, info_log, warn_log


USER_INFO = {'login_status': False, 'user_name': None}
DATA_DIR = os.path.join(config.BASE_DIR, 'db', 'data')
USER_DIR = os.path.join(os.path.abspath(DATA_DIR), 'user')
ADMIN_DIR = os.path.join(os.path.abspath(DATA_DIR), 'admin')

flag = True


def init():
    """
    初始化程序
    :return:
    """
    data_dir_list = os.listdir(os.path.join(os.path.abspath(DATA_DIR)))
    if 'admin' not in data_dir_list:
        os.makedirs(os.path.join(os.path.abspath(DATA_DIR), 'admin'))
        admin_info = {'user_name': 'admin', 'password': commons.md5('admin')}
        json.dump(admin_info, open(os.path.join(ADMIN_DIR, admin_info['user_name']), 'w', encoding='utf-8'))
        debug_log('初始化程序,创建admin用户')
    elif 'user' not in data_dir_list:
        os.makedirs(os.path.join(os.path.abspath(DATA_DIR), 'admin'))


def create_user():
    """
    创建账户
    :return:
    """
    user_name = input("请输入账户姓名:")
    bank_card = input("请输入绑定信用卡号:")
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() or bank_card not in user_list:
        password = getpass.getpass("请输入六位取款密码:")
        confirm_password = getpass.getpass("请再次输入密码:")
        if password.isdigit() and len(password) < 7 and password == confirm_password:
            os.makedirs(os.path.join(USER_DIR, bank_card, 'record'))
            user_info = {'user_name': user_name,
                         'card': bank_card,
                         'password': commons.md5(password),
                         'credit': 15000,
                         'balance': 15000,
                         'saving': 0,
                         'registered_date': str(datetime.date.today()),
                         'expire_date': str(datetime.date.today() + datetime.timedelta(days=365 * 10)),
                         'lock_status': 0,
                         'debt': []
            }
            json.dump(user_info, open(os.path.join(USER_DIR, bank_card, "user_info.json"), 'w', encoding='utf-8'))
            print("账户新建成功!")
            return True
        else:
            print("您的输入有误!")
    else:
        print("您的输入有误!")


def delelte_user():
    """
    删除账户
    :return:
    """
    bank_card = input("请输入银行卡号:")
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() and bank_card in user_list:
        os.remove(os.path.join(USER_DIR, bank_card,  'user_info.json'))
        user_record_list = os.listdir(os.path.join(USER_DIR, 'record'))
        for record_file in user_record_list:
            os.remove(os.path.join(USER_DIR, bank_card, 'record', record_file))
        os.rmdir(os.path.join(USER_DIR, bank_card))
        print("成功删除账户:[%s]" % bank_card)
        return True
    else:
        print("账户不存在!")


def login():
    """
    管理员登录
    :return:
    """
    user_name = input("请输入用户名:")
    password = getpass.getpass("请输入密码:")
    password = commons.md5(password)
    user_info = json.load(open(os.path.join(os.path.abspath(DATA_DIR), 'admin', 'admin'), 'r'))
    if user_name == user_info['user_name'] and password == user_info['password']:
        USER_INFO['login_status'] = True
        USER_INFO['user_name'] = user_name
        print("登录成功,欢迎您!")
        return True
    else:
        print("用户名或密码错误!")


def lock_bank_card():
    """
    锁定用户
    :return:
    """
    bank_card = input("请输入要锁定的银行卡:")
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() and bank_card in user_list:
        user_info = json.load(open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'r', encoding='utf-8'))
        user_info['lock_status'] = 1
        json.dump(user_info, open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'w', encoding='utf-8'))
        print("账户:%s已锁定" % bank_card)
        return True
    else:
        print("账户不存在!")


def no_lock_bank_card():
    """
    解锁用户
    :return:
    """
    bank_card = input("请输入要解锁的银行卡:")
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() and bank_card in user_list:
        user_info = json.load(open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'r', encoding='utf-8'))
        user_info['lock_status'] = 0
        json.dump(user_info, open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'w', encoding='utf-8'))
        print("账户:%s已解锁" % bank_card)
        return True
    else:
        print("账户不存在!")


def update_credit():
    """
    修改额度
    :return:
    """
    bank_card = input("请输入银行卡号:")
    new_credit = input("请输入调整后额度:")
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() and bank_card in user_list:
        user_info = json.load(open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'r', encoding='utf-8'))
        user_info['credit'] = int(new_credit)
        json.dump(user_info, open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'w', encoding='utf-8'))
        print("额度调整为:[\033[33m %s \033[0m]" % user_info['credit'])
        return True
    else:
        print("账户不存在!")


def dispaly_user_info():
    """
     查看用户信息
    :return:
    """
    bank_card = input("请输入用户银行卡号:")
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() and bank_card in user_list:
        user_info = json.load(open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'r', encoding='utf-8'))
        print("={:=^50}=".format("%s用户信息") % user_info['user_name'])
        print("|{:""<50}".format("用户姓名: %s") % user_info['user_name'])
        print("|{:""<50}".format("银行卡账户: %s") % user_info['card'])
        print("|{:""<50}".format("信用总额度: %s") % user_info['credit'])
        print("|{:""<50}".format("信用可使用额度: %s") % user_info['balance'])
        print("|{:""<50}".format("账户注册时间: %s") % user_info['registered_date'])
        print("|{:""<50}".format("账户到期时间: %s") % user_info['expire_date'])
        print("|{:""<50}".format("账户锁定状态: %s") % user_info['lock_status'])
        print("|{:""<50}".format("账户欠款: %s") % user_info['debt'])
        return True
    else:
        print("账户不存在!")


def quit():
    global flag
    flag = False


def main():
    menu_dict = {'1': create_user,
                 '2': delelte_user,
                 '3': update_credit,
                 '4': lock_bank_card,
                 '5': no_lock_bank_card,
                 '6': dispaly_user_info,
                 '7': quit
    }
    while flag:
        print("={:=^30}=".format("梁氏银行ATM后台"))
        print(("|{:^30}|".format("1.创建账户")))
        print("|{:^30}|".format("2.删除账户"))
        print("|{:^30}|".format("3.调整账户额度"))
        print("|{:^30}|".format("4.冻结账户"))
        print("|{:^30}|".format("5.解锁账户"))
        print("|{:^30}|".format("6.查看用户信息"))
        print("|{:^30}|".format("7.退出"))
        print("=" * 35)

        menu_input = input("请输入序号进行操作:").strip()
        if menu_input in menu_dict:
            menu_dict[menu_input]()
        else:
            print("输入有误!")


def run():
    init()
    if login():
        main()
