#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import os
import sys
import json
import getpass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.user import AdminUser
from lib.utils import md5

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
