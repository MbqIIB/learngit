#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import src_clinet



USER_INFO = {'login_status': False, 'user_name': None}


def check_login(func):
    def inner(*args, **kwargs):
        if USER_INFO['login_status']:
            func()
        else:
            print("请登录")


def check_admin():
    import json
    def inner(*args, **kwargs):
        user_name = USER_INFO['user_name']
        json


@check_login
src_clinet