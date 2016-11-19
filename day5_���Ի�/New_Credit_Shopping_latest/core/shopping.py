import json
import os
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_products = BASE_DIR + r"\database\goods_list"
db_shoping_car = BASE_DIR + r"\database\shopping_car"
db_user_info = BASE_DIR + r"\database\users_dict"
db_credit_info = BASE_DIR + r"\database\Credit_Info"
def Shopping_mall():
    shopping_list,pro_list  = [],[]
    with open(db_products, "r", encoding="utf-8") as  f_product:
        for item in f_product:
            pro_list.append(item.strip("\n").split())
    def pro_info():
        print("编号\t商品\t\t价格")
        for index, item in enumerate(pro_list,start=1):  #start表示默认从1开始
            print("%s\t\t%s\t\t%s" % (index, item[0], item[1]))
    while True:
            print(("\33[32;0m目前商城在售的商品信息\33[0m").center(40, "-"))
            pro_info()
            choice_id = input("\n\33[34;0m选择要购买的商品编号[购买ID]/[返回 b]\33[0m：")
            if choice_id.isdigit():
                choice_id = int(choice_id)
                if choice_id < len(pro_list) and choice_id >=0:
                    pro_item = pro_list[choice_id]
                    print("\33[31;0m商品%s加入购物车 价格%s\33[0m"%(pro_item[0],pro_item[1]))
                    shopping_list.append(pro_item)

                else:
                    print("\33[31;0m错误：没有相应的编号 请重新输入:\33[0m\n")
            elif  choice_id == "b":
                with open(db_shoping_car, "r+") as f_shopping_car:
                    list = json.loads(f_shopping_car.read())
                    list.extend(shopping_list)
                    f_shopping_car.seek(0)
                    f_shopping_car.truncate(0)
                    list = json.dumps(list)
                    f_shopping_car.write(list)
                break
            else:
                 print("\33[31;0m错误：没有相应的编号 请重新输入:\33[0m\n")
#购物函数
def Shopping_car():
    while True:
        with open(db_shoping_car, "r+") as f_shopping_car:
            list = json.loads(f_shopping_car.read())
            sum = 0
            print("\33[32;0m购物车信息清单\33[0m".center(40,"-"))
            for index,item in enumerate(list,start=1): #start=1表示标注从1开始
                print(index,item[0],item[1])
                sum +=int(item[1])
            print("\33[31;1m商品总额共计： %s\33[0m"%(sum))
        if_buy = input("\n\33[34;0m选择要进行的操作 返回[b]\33[0m:")
        if if_buy == "b" :
            break
#清空购物车函数
def ClearShoppCars():

    with open(db_shoping_car, "w") as f_shopping_car:
        list = json.dumps([])
        f_shopping_car.write(list)
#商品付款函数
def PayShopping(current_user):
    sum = 0
    with open(db_shoping_car ,"r+",encoding="utf8") as file:
        price_file = json.loads(file.read())
        for price in price_file:
            # print(price[1])
            sum += int(price[1])  #商品价格累加起来，商品价格的总和
            # Credit_Number = input("请输入你的卡号:")
            # Credit_Password = input("请输入你的卡号密码")
        if_pay = input("\n\n\33[34;0m当前商品总额：%s 是否进行支付 确定[y]/返回[b]\33[0m:" % (sum))
        while True:
            if if_pay == "y":
                Credit_Number = input("请输入你的卡号:")
                Credit_Password = input("请输入你的卡号密码:")
                # with open(db_credit_info,"r+",encoding="utf8") as credit_file:
                credit_file = open(db_credit_info, "r+", encoding="utf8")
                Credit_info = json.loads(credit_file.read())
                User_limit = Credit_info[current_user]["defaultlimit"]
                if Credit_Number == Credit_info[current_user]["creditcard"] and Credit_Password == Credit_info[current_user]["password"]:
                    print("卡号账号密码通过，请继续支付")
                    if sum < int(User_limit):
                        Left_Limit = int(User_limit) - int(sum)
                        print("你买的所有物品已经付款，总共付了%s,你还剩%s" % (sum, Left_Limit))
                        # if current_user in _info.keys():
                        Credit_info[current_user]["defaultlimit"] = Left_Limit  # 把剩下的额度赋值给原来的key
                        dict = json.dumps(Credit_info)
                        credit_file.seek(0)
                        credit_file.truncate(0)  # 把原文件清空
                        credit_file.write(dict)  # 再写入更改后的文件
                        credit_file.close()
                        # user_file.write((json.dumps([])))
                        # user_file.write(json.dumps(user_info))
                        ClearShoppCars()  # 支付完就清空购物车
                        break
                    else:
                        print("你的信用卡额度不够,如果需要继续付款，您可以选择透支付款")
                        #充值函数
                        if_recharge = input("\n\n\33[34;0m你是否要透支付款，确定[y]/返回[b]\33[0m:")
                        if if_recharge == "y":
                            #可透支金额
                            Can_limit = Credit_info[current_user]["limit"]
                            if sum < int(Can_limit):
                                Left_Can_limit = int(Can_limit) - int(sum)
                                print("你买的所有物品已经付款，总共付了%s,你的透支余额还剩%s" % (sum, Left_Can_limit))
                                credit_file = open(db_credit_info, "r+", encoding="utf8")
                                Credit_info = json.loads(credit_file.read())
                                Credit_info[current_user]["limit"] = Left_Can_limit # 把剩下的额度赋值给原来的key
                                dict = json.dumps(Credit_info)
                                credit_file.seek(0)
                                credit_file.truncate(0)  # 把原文件清空
                                credit_file.write(dict)
                                credit_file.close()
                                # 再写入更改后的文件
                                # user_file.write((json.dumps([])))
                                # user_file.write(json.dumps(user_info))
                                ClearShoppCars()  # 支付完就清空购物车
                                break

                                    # break
                            else:
                                print("可透支的金额也无法完成付款，你这么买买买，你爸妈知道吗？")
                                break

                else:
                    print("账号或密码失败，请重新输入")






