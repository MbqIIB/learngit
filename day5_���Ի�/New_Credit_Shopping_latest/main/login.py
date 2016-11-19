#!/usr/bin/env python
import os
import json
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)
from core import menu
from core import shopping
from core import creditcard
#数据库文件相对路径
db_users_dict = BASE_DIR + r"\database\users_dict"
while True:
    print("\33[31;0m欢迎来到**购物中心,请输入用户名和密码\33[0m")
    username = input("\33[34;0m请输入用户名：\33[0m")
    password = input("\33[34;0m请输入密码：\33[0m")
    if len(username.strip()) > 0: #判断输入是否为空，为空就显示失败，不为空执行下面程序
        with open(db_users_dict, "r+",encoding="utf8") as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            # print(users_dict.keys())
            if username in users_dict.keys():
                global current_user
                current_user = username  #记录当前登录的用户名，后面有需要把这个参数传出去
                if password == users_dict[username]["password"]:
                    if users_dict[username]["locked"] == 0:
                        print("\33[31;0m用户 %s 认证成功\33[0m" % (username))
                        menu.menushow(current_user)  #调用显示菜单
                    else:
                        print("\33[31;0m用户 %s 已经被锁定 认证失败\33[0m" % (username))
                else:
                    print("\33[31;0m输入的密码不匹配 认证失败\33[0m")
            else:
                print("\33[31;0m输入的用户名不存在 认证失败\33[0m")
    else:
        print("\33[31;0m输入的用户名为空 认证失败\33[0m")
        continue



