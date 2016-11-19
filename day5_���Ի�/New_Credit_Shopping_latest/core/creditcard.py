#!/usr/bin/env python
#coding=utf8
import os
import sys
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
db_credit_info = BASE_DIR + r"\database\Credit_Info"
# username = "liuhuihuang"
def quxian(current_user):
    while True:
        credit_file = open(db_credit_info, "r+", encoding="utf8")
        credit_info = json.loads(credit_file.read())
        if current_user in credit_info.keys():
                LimitTotal = credit_info[(current_user)]["defaultlimit"]
                # print("你的信用卡额度为:%s" % (LimitTotal))
                if_quxian = input("是否要取现，是就按[y],否就按[b]:")
                if if_quxian == "y":
                    Money_input = int(input("请输入你要取现的金额:"))
                    if Money_input > int(LimitTotal):
                         print("你的额度不够，请输入在%s以下的金额" %(LimitTotal))
                    elif Money_input == 0:
                        print("你输入的金额为0，无法提现")
                    else:
                        Interest = int(Money_input * 0.05)
                        LeftLimit = int(int(LimitTotal) - (int(Interest) + int(Money_input)))
                        credit_info[current_user]["defaultlimit"] = LeftLimit  # 把剩下的额度赋值给原来的key
                        dict = json.dumps(credit_info)
                        credit_file.seek(0)
                        credit_file.truncate(0)  # 把原文件清空
                        credit_file.write(dict)
                        # LimitTotal = LeftLimit
                        # LeftLimit = json.dumps(user_file.write()
                        print("你取现金额为%s,利息为%s,你的额度还剩%s" %(Money_input, Interest,LeftLimit))
                        break
                if if_quxian == "b":
                    break
#此函数为转账函数，为了简单，把用户直接定义了在程序中了，没有采用传参的方法
def zhuanzhang():
    username = "liuhuihuang"
    othername = "alex"
    while True:
        with open(db_credit_info , "r+", encoding="utf8") as Credit_file:
            credit_info = json.loads(Credit_file.read())
            # print(credit_info[username]["defaultlimit"])
            print("\33[32;0m转账\33[0m".center(40, "-"))
            if_trans = input("\n\33[34;0m是否进行转账 确定[y]/返回[b]\33[0m:")
            if if_trans == "y":
                Credit_Card = input("请输入卡号:")
                Credit_Password = input("请输入卡号密码:")
                if Credit_Card == credit_info[username]["creditcard"] and Credit_Password == credit_info[username][
                    "password"]:
                    print("验证通过")
                    Transfer_Money = int(input("请输入你要转账的金额:"))
                    if Transfer_Money > credit_info[username]["defaultlimit"]:
                        print("用户%s额度不足" % (username))
                        continue
                    Transfer_Credit = input("请输入你要转账的卡号:")
                    if Transfer_Credit == credit_info[othername]["creditcard"]:
                        credit_info[othername]["defaultlimit"] += Transfer_Money
                        # print(credit_info[othername]["defaultlimit"])
                        credit_info[username]["defaultlimit"] -= Transfer_Money
                        dict = json.dumps(credit_info)
                        Credit_file.seek(0)
                        Credit_file.truncate(0)  # 把原文件清空
                        Credit_file.write(dict)
                        print("用户%s给卡号为%s的用户%s转了%s元,用户%s的余额为%s元,用户%s的余额为%s元" % (
                        username, Transfer_Credit, othername, Transfer_Money,
                        username, credit_info[username]["defaultlimit"], othername,
                        credit_info[othername]["defaultlimit"]))
                        break
                        # print(credit_info[username]["defaultlimit"])
                    else:
                        print("对方卡号输入错误，请确认后再重新输入")
                else:
                    print("账号或者密码不正确，请确认后再重新输入")
            else:
                if if_trans == "b":
                    break


def huankuan(current_user):
    while True:
        with open(db_credit_info, "r+", encoding="utf8") as Credit_file:
            credit_info = json.loads(Credit_file.read())
            # print(credit_info[username]["defaultlimit"])
            print("\33[32;0m还款\33[0m".center(40, "-"))
            if_give = input("\n\33[34;0m是否进行还款 确定【y】/返回【b】\33[0m:")
            if if_give == "y":
                Credit_Card = input("请输入卡号:")
                Credit_Password = input("请输入卡号密码:")
                if Credit_Card == credit_info[current_user]["creditcard"] and Credit_Password == credit_info[current_user][
                    "password"]:
                    print("验证通过")
                    Transfer_Money = int(input("请输入你想还款的金额:"))
                    credit_info[current_user]["debet"] = Transfer_Money - credit_info[current_user]["debet"]
                    if credit_info[current_user]["debet"] > 0:
                        print("你的欠费已还清")
                        credit_info[current_user]["debet"] = 0
                        # break
                        dict = json.dumps(credit_info)
                        Credit_file.seek(0)
                        Credit_file.truncate(0)  # 把原文件清空
                        Credit_file.write(dict)
                    else:
                        # credit_info[username]["debet"] -= Transfer_Money
                        print("已经还了%s元,还欠%s" % (Transfer_Money, abs(credit_info[current_user]["debet"])))
                        dict = json.dumps(credit_info)
                        Credit_file.seek(0)
                        Credit_file.truncate(0)  # 把原文件清空
                        Credit_file.write(dict)
                        break
                else:
                    print("账号或者密码输入错误，请确认后再重新输入")
            else:
                if if_give == "b":
                    break

#日志记录函数
def login_record(current_user):
    pass
