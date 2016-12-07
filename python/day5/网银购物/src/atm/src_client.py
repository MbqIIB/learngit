#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import os
import datetime
import json
import getpass
import time

# 加载配置文件
from etc import config
from lib import commons


USER_INFO = {'login_status': False, 'user_name': None, 'bank_card': None}

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
    elif 'user' not in data_dir_list:
        os.makedirs(os.path.join(os.path.abspath(DATA_DIR), 'admin'))


def login():
    """
    用户登录
    :return:
    """
    user_name = input("请输入账户姓名:")
    bank_card = input("请输入绑定信用卡号:")
    password = getpass.getpass("请输入六位取款密码:")
    password = commons.md5(password)
    user_list = os.listdir(USER_DIR)
    if bank_card.isdigit() or bank_card not in user_list:
        user_info = json.load(open(os.path.join(USER_DIR, bank_card, 'user_info.json'), 'r', encoding='utf-8'))
        if user_name == user_info['user_name'] and password == user_info['password']:
            USER_INFO['login_status'] = True
            USER_INFO['user_name'] = user_name
            USER_INFO['bank_card'] = bank_card
            print("登录成功,欢迎您!")
            return True
        else:
            print("用户名或密码错误!")
    else:
        print("用户名或密码错误!")



def update_password():
    """
    修改取款密码
    :return:
    """
    password = getpass.getpass("请输入六位取款密码:")
    password = commons.md5(password)
    user_info = json.load(open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
    if password == user_info['password']:
        new_password = getpass.getpass("请输入新的六位取款密码")
        confirm_password = getpass.getpass("请再次输入密码:")
        if new_password.isdigit() and len(new_password) < 7 and new_password == confirm_password:
            password = commons.md5(new_password)
            user_info['password'] = password
            json.dump(user_info, open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'w', encoding='utf-8'))
            print("密码已修改")
            return True
    else:
        print("账户或密码错误")


def pay_balance(balance, bank_card=None):
    """
    支付接口
    :param balance:
    :return:
    """
    if bank_card:
        USER_INFO['bank_card'] = bank_card
    user_list = os.listdir(USER_DIR)
    if USER_INFO['bank_card'] and USER_INFO['bank_card'] in user_list:
        password = getpass.getpass("请输入六位取款密码:")
        password = commons.md5(password)
        user_info = json.load(open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
        if password == user_info['password']:
            if user_info['balance'] > balance:  # 因为会先扣saving的,所以只要判断balance金额就行
                if 0 < user_info['saving'] < balance:
                    balance -= user_info['saving']
                    user_info['saving'] = 0
                    user_info['balance'] -= balance
                    if not user_info['debt']: # 是不是空列表的
                        debt_dict = {time.strftime('%Y-%m'): balance}
                        user_info['debt'].append(debt_dict)
                    if int(time.strftime('%d')) <= 22:  # 设置一个触发点,每个月10号创建这个月账单
                        for debt_dict in user_info['debt']:
                            time_list = time.strftime('%Y-%m').split('-')
                            last_month = int(time_list[1]) - 1
                            new_time = '-'.join(time_list[0], last_month)
                            if new_time in list(debt_dict.keys()):  # 判断这个月是否有欠款字典
                                debt_dict[time.strftime('%Y-%m')] += balance
                            else:
                                debt_dict = {new_time: balance}
                                user_info['debt'].append(debt_dict)
                    elif int(time.strftime('%d')) >= 22:
                        for debt_dict in user_info['debt']:
                            if time.strftime('%Y-%m') in list(debt_dict.keys()):  # 判断这个月是否有欠款字典
                                debt_dict[time.strftime('%Y-%m')] += balance
                            else:
                                debt_dict = {time.strftime('%Y-%m'): balance}
                                user_info['debt'].append(debt_dict)
                elif user_info['saving'] > balance:
                    user_info['saving'] -= balance
                    balance -= user_info['saving']
                else:
                    user_info['balance'] -= balance
                    if not user_info['debt']:  # 是不是空列表的,表示有没有欠款
                        debt_dict = {time.strftime('%Y-%m'): balance}
                        user_info['debt'].append(debt_dict)
                    if int(time.strftime('%d')) <= 22:  # 设置一个触发点,每个月22号创建这个月账单
                        for debt_dict in user_info['debt']:
                            time_list = time.strftime('%Y-%m').split('-')
                            last_month = int(time_list[1]) - 1
                            new_time = '-'.join(time_list[0], last_month)
                            if new_time in list(debt_dict.keys()):  # 判断这个月是否有欠款字典
                                debt_dict[time.strftime('%Y-%m')] += balance
                            else:
                                debt_dict = {new_time: balance}
                                user_info['debt'].append(debt_dict)
                    elif int(time.strftime('%d')) >= 22:
                        for debt_dict in user_info['debt']:
                            if time.strftime('%Y-%m') in list(debt_dict.keys()):  # 判断这个月是否有欠款字典
                                debt_dict[time.strftime('%Y-%m')] += balance
                            else:
                                debt_dict = {time.strftime('%Y-%m'): balance}
                                user_info['debt'].append(debt_dict)
                json.dump(user_info, open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'w', encoding='utf-8'))
                print("当前账户金额:[\033[33m %s \033[0m]" % user_info['balance'])
                print("当前账户存款:[\033[33m %s \033[0m]" % user_info['saving'])
                return True
            else:
                print("您的金额不足")
                return False
        else:
            print("密码有误.")
            return False
    else:
        print("账户不存在")
        return False


def get_balance():
    """
    账户提现
    :return:
    """
    balance = int(input("请输入提现金额:"))
    user_list = os.listdir(USER_DIR)
    if USER_INFO['bank_card'].isdigit() and USER_INFO['bank_card'] in user_list:
        user_info = json.load(open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
        if user_info['balance'] > balance or user_info['saving'] > balance:
            if 0 < user_info['saving'] <= balance:
                balance -= user_info['saving']
                user_info['saving'] = 0
                user_info['balance'] -= balance
            elif user_info['saving'] > balance:
                user_info['saving'] -= balance
            else:
                user_info['balance'] -= balance + balance * 0.05
            json.dump(user_info, open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'w', encoding='utf-8'))
            print("当前账户金额:[\033[33m %s \033[0m]" % user_info['balance'])
            print("当前账户存款:[\033[33m %s \033[0m]" % user_info['saving'])
            return True
        else:
            print("您的金额不足")
            return False
    else:
        print("账户不存在!")


def move_balance():
    """
    账户转账
    :return:
    """
    des_bank_card = input("请输入对方账号:")
    balance = int(input("请输入转账金额:"))
    user_info = json.load(open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
    des_user_info = json.load(open(os.path.join(USER_DIR, des_bank_card, 'user_info.json'), 'r', encoding='utf-8'))
    if user_info['balance'] > balance or user_info['saving'] > balance:
        if 0 < user_info['saving'] < balance:
            balance -= user_info['saving']
            user_info['saving'] = 0
            user_info['balance'] -= balance
            if des_user_info['balance'] >= des_user_info['credit']:
                des_user_info['saving'] += balance
            else:
                debt_balance = des_user_info['credit'] - des_user_info['balance']
                des_user_info['balance'] += debt_balance
                des_user_info['saving'] += balance - debt_balance
        elif user_info['saving'] > balance:
            user_info['saving'] -= balance
            if des_user_info['balance'] >= des_user_info['credit']:
                des_user_info['saving'] += balance
            else:
                debt_balance = des_user_info['credit'] - des_user_info['balance']
                des_user_info['balance'] += debt_balance
                des_user_info['saving'] += balance - debt_balance
        else:
            user_info['balance'] -= balance
            if des_user_info['balance'] >= des_user_info['credit']:
                des_user_info['saving'] += balance
            else:
                debt_balance = des_user_info['credit'] - des_user_info['balance']
                des_user_info['balance'] += debt_balance
                des_user_info['saving'] += balance - debt_balance
        json.dump(user_info, open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'w', encoding='utf-8'))
        json.dump(des_user_info, open(os.path.join(USER_DIR, des_bank_card, 'user_info.json'), 'w', encoding='utf-8'))
        print("当前账户金额:[\033[33m %s \033[0m]" % user_info['balance'])
        print("当前账户存款:[\033[33m %s \033[0m]" % user_info['saving'])
        return True
    else:
        print("您的金额不足")
        return False


def saving_balance():
    """
    存款,账户充值,还款
    :return:
    """
    balance = int(input("请输入存款金额:"))
    user_info = json.load(open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
    if user_info['balance'] < user_info['credit']:  # 金钱小于额度
        debt_balance = user_info['credit'] - user_info['balance']
        if balance >= debt_balance:
            user_info['balance'] = user_info['credit']  # 还清欠款
            saving_balace = balance - debt_balance
            user_info['saving'] += saving_balace
        else:
            user_info['balance'] += balance
        if user_info['debt']:  # 是不是空列表的
            record_dir = os.path.join(USER_DIR, USER_INFO['bank_card'], 'record')
            record_dir_list = os.listdir(record_dir)
            for record_time in record_dir_list:
                time_list = record_time.split('-')
                del time_list[2]
                record_time = '-'.join(time_list)
                for debt_dict in user_info['debt']:
                    if record_time in list(debt_dict.keys()):
                        if debt_dict[record_time] > balance:
                            debt_dict[record_time] -= balance
                            balance = 0
                        elif debt_dict[record_time] < balance:
                            balance -= debt_dict[record_time]
                            dict_index = user_info['debt'].index(debt_dict)
                            del user_info['debt'][dict_index]
                            print("%s账单已还清" % record_time)
                            continue
            user_info['saving'] += balance
    else:
        user_info['saving'] += balance
    json.dump(user_info, open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'w', encoding='utf-8'))
    print("当前账户金额:[\033[33m %s \033[0m]" % user_info['balance'])
    print("当前账户存款:[\033[33m %s \033[0m]" % user_info['saving'])
    return True


def show_balance(bank_card=None):
    """
    查看余额
    :return: 返回银行卡总金额(saving + balance)
    """
    if bank_card:
        USER_INFO['bank_card'] = bank_card
        user_list = os.listdir(USER_DIR)
        if USER_INFO['bank_card'] and USER_INFO['bank_card'] in user_list:
            user_info = json.load(open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
            return user_info['balance'] + user_info['saving']
        else:
            print("账号不存在")
            return False
    else:
        user_list = os.listdir(USER_DIR)
        if USER_INFO['bank_card'] and USER_INFO['bank_card'] in user_list:
            user_info = json.load(
                open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
            balance = user_info['balance'] + user_info['saving']
            print("您当前余额为[%s]" % balance)
        else:
            print("账号不存在")
            return False


def show_debt():
    user_list = os.listdir(USER_DIR)
    if USER_INFO['bank_card'] and USER_INFO['bank_card'] in user_list:
        user_info = json.load(
            open(os.path.join(USER_DIR, USER_INFO['bank_card'], 'user_info.json'), 'r', encoding='utf-8'))
        print('{:=^50}'.format('欠款清单'))
        print('|{: <25}{: <25}|'.format('欠款时间', '欠款金额'))
        for debt_dict in user_info['debt']:
            debt_list = list(debt_dict.keys())
            for debt in debt_list:
                print('|{: <25}{: <25}|'.format(debt, debt_dict[debt]))
    else:
        print("账号不存在")
        return False


def quit():
    global flag
    flag = False


def main():
    menu_dict = {'1': move_balance,
                 '2': get_balance,
                 '3': saving_balance,
                 '4': show_debt,
                 '5': show_balance,
                 '6': update_password,
                 '7': quit,
    }
    while flag:
        print("={:=^30}=".format("梁氏银行ATM"))
        print(("|{:^30}|".format("1.转账")))
        print("|{:^30}|".format("2.提现"))
        print("|{:^30}|".format("3.还款"))
        print("|{:^30}|".format("4.查询欠款"))
        print("|{:^30}|".format("5.查询余额"))
        print("|{:^30}|".format("6.修改密码"))
        print("|{:^30}|".format("7.退出"))
        print("=" * 35)

        menu_input = input("请输入序号进行操作:").strip()
        if menu_input in menu_dict:
            menu_dict[menu_input]()
        else:
            print("输入有误!")


def run():
    if login():

        main()
