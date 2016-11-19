import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
db_users_info = BASE_DIR + r"\database\users_dict"
#注册用户模块，这里注册后就会报一个异常，直接退出程序了，先不管了
def register(locked=0,creditcard=0):
    while True:
        # name_list =[]

        with open(db_users_info, "r+") as f_users_dict:
            users_info = json.loads(f_users_dict.read())
            for key in users_info.keys():
                print("系统已有用户[%s]" % (key))
            # for username in users_info:
            #     name_list.append(username)
            # for name in name_list:
            #     print("系统中已有用户%s" %(name))
                if_create = input("\n\33[34;0m是否创建新的用户 确定[y]/返回[b]\33[0m:")
                if if_create == "y":
                    Create_Name = input("请输入要创建的用户名:")
                    Create_Passwd = input("请输入要创建的密码:")
                    if Create_Name not in users_info.keys():
                        if len(Create_Name.strip()) > 0:
                            if len(Create_Passwd.strip()) > 0:
                                users_info[Create_Name] = {"username": Create_Name, "password": Create_Passwd,
                                                        "creditcard": creditcard,"locked": locked}
                                dict = json.dumps(users_info)
                                f_users_dict.seek(0)
                                f_users_dict.truncate(0)
                                f_users_dict.write(dict)
                                print("\33[31;1m创建用户 %s 成功\33[0m\n" % (Create_Name))
                            else:
                                print("\33[31;0m输入的密码为空\33[0m\n")
                        else:
                            print("\33[31;0m输入的用户名为空\33[0m\n")
                    else:
                        print("\33[31;0m用户名 %s 已经存在\33[0m\n" % (Create_Name))
                    if if_create == "b":
                        break





