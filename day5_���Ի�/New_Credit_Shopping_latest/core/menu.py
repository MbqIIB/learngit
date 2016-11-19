import os
import sys
from core import shopping
from core import creditcard
from core import register_user
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
def menushow(current_user):
    print("\33[35;1m欢迎进入信用卡购物模拟程序\33[0m".center(50, "#"),
    "\n1 购物中心\n"
    "2 取现\n"
    "3 还款\n"
    "4 转账\n"
    "5 查看ATM操作日志\n"
    "6 注册用户\n"
    "q 退出程序\n")
    user_choice = input("请输入你的选择>>: ").strip()
    # global current_user
    # current_user = username
    if len(user_choice) == 0:
        print("温馨提示:请输入[1-4]或[q]")
    if user_choice == "1":
        while True:
            print("\33[36;1m欢迎进入购物中心\33[0m".center(50, "*"),
                  "\n1 购物商场\n"
                  "2 查看购物车\n"
                  "3 购物结算\n"
                  "4 清空购物车\n"
                  "b 返回\n")
            choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
            if choice_id == "1":
                shopping.Shopping_mall()
            elif choice_id == "2":
                shopping.Shopping_car()
            elif choice_id == "3":
                shopping.PayShopping(current_user)
            elif choice_id == "4":
                shopping.ClearShoppCars()
            elif choice_id == "b":
                menushow(current_user) #跳回主菜单
    elif user_choice == "2":
            while True:
                print("\33[36;1m欢迎进入取现中心\33[0m".center(50, "*"),
                    "\n1 信用卡取现\n"
                    "b 返回\n")
                choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
                if choice_id == "1":
                    creditcard.quxian(current_user)
                elif choice_id == "b":
                    menushow(current_user) #跳回主菜单
    elif user_choice == "3":
        while True:
            print("\33[36;1m欢迎进入还款中心\33[0m".center(50, "*"),
                  "\n1 信用卡还款\n"
                  "b 返回\n")
            choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
            if choice_id == "1":
                creditcard.huankuan(current_user)
            elif choice_id == "b":
                menushow(current_user)  # 跳回主菜单
    elif user_choice == "5":
        while True:
            print("\33[36;1m欢迎进入日志记录中心\33[0m".center(50, "*"),
                  "\n1 查看日志记录\n"
                  "b 返回\n")
            choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
            if choice_id == "1":
                creditcard.login_record(current_user)
            elif choice_id == "b":
                menushow(current_user)  # 跳回主菜单

    elif user_choice == "4":
        while True:
            print("\33[36;1m欢迎进入转账中心\33[0m".center(50, "*"),
                  "\n1 信用卡转账\n"
                  "b 返回\n")
            choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
            if choice_id == "1":
                creditcard.zhuanzhang()
            elif choice_id == "b":
                menushow(current_user)
    elif user_choice == "6":
        while True:
            print("\33[36;1m欢迎来到注册用户中心\33[0m".center(50, "*"),
                  "\n1 用户注册\n"
                  "b 返回\n")
            choice_id = input("\33[34;0m选择要进入模式的ID\33[0m:")
            if choice_id == "1":
                register_user.register(locked=0,creditcard=0)
            elif choice_id == "b":
                menushow(current_user)


    elif user_choice == "q":
        exit()
