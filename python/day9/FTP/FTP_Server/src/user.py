#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import os
import sys
import json
import getpass

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from lib.utils import md5
from lib.utils import Config

class AdminUser:

    def __init__(self):
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'etc', 'config.ini')
        self.CONFIG = Config(config_path, section='SERVER')
        self.data = self.CONFIG.data_path
        self.user_db = os.path.join(self.CONFIG.db_path, 'user.json')
        self.user_path = None
        self.dir_size = int(self.CONFIG.dir_size.split()[0]) * 1024 * 1024

        # 判断用户json文件是否存在,如果不存在则初始化用户json文件
        if not os.path.exists(self.user_db):
            user_dict = {'admin': {'password': md5('admin'),
                                   'dir_size': self.dir_size,
                                   'super_user': '1',
                                   'lock_status': '0',
                                   'user_dir': os.path.join(self.data, 'admin')
                                   }
                         }
            json.dump(user_dict, open(self.user_db, 'w'))
            user_home = os.path.join(self.data, 'admin')
            os.mkdir(user_home)  # 创建管理员家目录

    def registered(self, user, password):
        """
        注册用户
        :param user: 用户名
        :param password: 用户密码
        :return: 注册用户成功/失败
        """
        user_dict = json.load(open(self.user_db, 'r'))

        user_list = list(user_dict.keys())
        if user in user_list:
            return False

        user_dict[user] = {'password': password,
                           'dir_size': self.dir_size,
                           'super_user': '0',
                           'lock_status': '0',
                           'user_dir': os.path.join(self.data, user)
                           }

        json.dump(user_dict, open(self.user_db, 'w'))
        user_home = os.path.join(self.data, user)
        os.mkdir(user_home)  # 创建用户家目录
        return True

    def login(self, user, password):
        """
        用户登陆
        :param user: 用户名
        :param password: 用户密码
        :return: 登陆成功/失败
        """
        user_dict = json.load(open(self.user_db, 'r'))

        user_list = list(user_dict.keys())
        if user not in user_list:
            return False

        if user_dict[user]['password'] == password:
            self.user_path = os.path.join(self.data, user)
            return True

    def change_password(self, user, password):
        """
        修改用户密码
        :param user:  用户名
        :param password:  用户密码
        :return: 修改密码成功/失败
        """

        user_dict = json.load(open(self.user_db, 'r'))
        user_list = list(user_dict.keys())
        if user not in user_list:
            return False

        user_dict[user]['password'] = password
        return True

    def del_user(self, user):
        """
        删除用户
        :param user: 用户名
        :return: 删除用户成功/失败
        """
        user_dict = json.load(open(self.user_db, 'r'))
        user_list = list(user_dict.keys())
        if user not in user_list:
            return False

        del user_dict[user]
        return True

    def lock_user(self, user):
        """
        锁定用户
        :param user: 用户名
        :return: 锁定用户成功/失败
        """
        user_dict = json.load(open(self.user_db, 'r'))
        user_list = list(user_dict.keys())
        if user not in user_list:
            return False

        user_dict[user]['lock'] = '1'
        return True

    def change_user_permissions(self, user, permissions):
        user_dict = json.load(open(self.user_db, 'r'))
        user_list = list(user_dict.keys())
        if user not in user_list:
            return False

        user_dict[user]['super_user'] = permissions
        return True

    def change_user_container_size(self, user, container_size):
        user_dict = json.load(open(self.user_db, 'r'))
        user_list = list(user_dict.keys())
        if user not in user_list:
            return False

        user_dict[user]['dir_size'] = container_size
        return True

    def run(self):
        """
        管理用户信息
        :return: 修改用户信息成功/失败
        """
        admin_menu = '''
        ============================================
        |               1.创建用户                  |
        |               2.修改密码                  |
        |               3.删除用户                  |
        |               4.修改权限                  |
        |               5.锁定用户                  |
        |               6.修改空间                  |
        ============================================
        '''
        print(admin_menu)
        admin_input = input("请输入菜单中操作:")
        if admin_input == '1':
            user = input('请输入用户名:')
            password = md5(getpass.getpass('请输入密码:'))
            if self.registered(user, password):
                print("创建用户成功!")
            else:
                print("创建用户失败!")
        elif admin_input == '2':
            user = input('请输入用户名:')
            password = md5(getpass.getpass('请输入新的密码:'))
            if self.change_password(user, password):
                print("修改密码成功!")
            else:
                print("修改密码失败!")
        elif admin_input == '3':
            user = input('请输入用户名:')
            if self.del_user(user):
                print("删除用户成功!")
            else:
                print("删除用户失败!")
        elif admin_input == '4':
            user = input('请输入用户名:')
            permissions = input("请输入数字(0:管理员|1:普通用户):")
            if self.change_user_permissions(user, permissions):
                print("修改权限成功!")
            else:
                print("修改权限失败!")
        elif admin_input == '5':
            user = input('请输入用户名:')
            if self.lock_user(user):
                print("锁定用户成功!")
            else:
                print("锁定用户失败!")
        elif admin_input == '6':
            user = input('请输入用户名:')
            size = input("请输入修改后大小:")
            if self.change_user_container_size(user, size):
                print("修改空间成功!")
            else:
                print("修改空间失败!")
        elif admin_input == 'exit':
            sys.exit(0)
        else:
            print("输入有误!")


if __name__ == '__main__':
    admin_obj = AdminUser()
    user = input('请输入管理员用户名:')
    password = getpass.getpass('请输入密码:')

    if not admin_obj.login(user, md5(password)):
        print("用户名或密码错误")
        sys.exit(1)

    user_dict = json.load(open(admin_obj.user_db, 'r'))
    if user_dict[user]['super_user'] == '1':
        admin_obj.run()



