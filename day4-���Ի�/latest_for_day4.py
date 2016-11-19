#!/usr/bin/env python
# coding=utf8
import os, re
#这里我把查询这块分为3个函数了,纠结了很久是放一起还是分开，最后还是分开了，容易写一些
def search_age_above_22():   #定义年纪大于22岁函数
    new = []  # 把读取到的文件写入至此列表
    temp = []  # 记录查询年龄大于22岁的总数列表

    with open("Information.txt", "r", encoding="utf8") as file:
        for line in file.readlines():
            new.append(line.strip().split(","))
        for each_line in new:
            if each_line[2] > "22":
                temp.append(each_line[2])
                print(each_line[1:3])
        print("查到年龄大于22岁的总数为:%s" % len(temp))

def search_depot_of_IT():  #定义部门为IT的函数
    new = []  # 把读取到的文件写入至此列表
    temp = []  # 记录查询部门为IT的总数列表
    with open("Information.txt", "r", encoding="utf8") as file:
        for line in file.readlines():
            new.append(line.strip().split(","))
        for each_line in new:
            if each_line[4] == "IT":
                temp.append(each_line[4])
                print(str(each_line[::]))
        print("查到部门为IT的总数为:%s" % len(temp))

def search_date_of_2013():  #定义开始工作日期为2013年的函数
    new = []  # 把读取到的文件写入至此列表
    temp = []  # 记录查询开始工作日期为2013年的总数列表
    with open("Information.txt", "r", encoding="utf8") as file:
        for line in file.readlines():
            new.append(line.strip().split(","))
    for each_line in new:
        if re.search("2013", each_line[-1]):
            temp.append(each_line[5])
            print(each_line[::])
    print("查到工作时间在2013年名单总数为:%s" % len(temp))

def add():   #定义增加函数
    new = []  # 把读取到的文件写入至此列表
    temp = [] #此列表为了自增而建，代码写的很low
    user_input = str(input("请输入类似于[吴东杭,21,17710890829,运维,1995-08-29]的一串东西:"))
    with open("Information.txt", "r", encoding="utf8") as read_file, open("NewInformation.txt", "w+",
                                                                          encoding="utf8")as write_file:
        for line in read_file:
            new.append(line.strip().split(","))
        for new_line in new:
            # i.append(j)
            temp.append(new_line)
            # print(i[-1][0])
        Added_Data = "%d,%s" % (int(temp[-1][0]) + 1, user_input)
        temp.append(Added_Data.split(','))
        for each_line in temp:
            write_file.write(','.join(each_line).strip(""))  # 通过内置方法join把列表转换为字符串
            write_file.write("\n")  # 写入这行，可使文件换行
    os.rename("Information.txt", "Information.bak")
    os.rename("NewInformation.txt", "Information.txt")
    os.remove("Information.bak")

def delete():  #定义删除函数
    ReadFile = []
    User_Choice = int(input("请输入staff_id号:"))
    with open("Information.txt", "r", encoding="utf8") as read_file, open("NewInformation.txt", "w+",
                                                                          encoding="utf8") as write_file:
        for line in read_file:
            ReadFile.append(line.strip().split(","))
        for each_line in ReadFile:
            if User_Choice == int(each_line[0]):
                ReadFile.remove(ReadFile[User_Choice - 1])
                for new_line in ReadFile:
                    write_file.write(','.join(new_line).strip(""))  # 通过内置方法join把列表转换为字符串
                    write_file.write("\n")  # 写入这行，可使文件换行
    os.rename("Information.txt", "Information.bak")
    os.rename("NewInformation.txt", "Information.txt")
    os.remove("Information.bak")

def modify():  #定义更改函数
    if not os.path.exists("Information.txt"):
        exit(-1)
    User_Input = str(input("请输入:"))
    with open("Information.txt", "r", encoding="utf8") as read_file, open("NewInformation.txt", "w+",
                                                                          encoding="utf8") as write_file:
        for line in read_file.readlines():
            write_file.write(line.replace("IT", User_Input))
    os.rename("Information.txt", "Information.bak")
    os.rename("NewInformation.txt", "Information.txt")
    os.remove("Information.bak")

if __name__ == '__main__':
    msg = '''
       1：查询年龄大于22岁学生信息
       2：查询部门为IT学生信息
       3：查询工作开始时间在2013年学生信息
       4：添加
       5：删除
       6：修改
       7：退出
       '''
    menu_dic = {

        '1': search_age_above_22,
        '2': search_depot_of_IT,
        '3': search_date_of_2013,
        '4': add,
        '5': delete,
        '6': modify,
        '7': exit,
    }
    while True:
        print(msg)
        choice = input("操作>>: ").strip()
        if len(choice) == 0 or choice not in menu_dic or choice.isalpha():
            print("温馨提示:请输入1-7之间的数字")
            continue
        if choice == '7': break
        menu_dic[choice]()