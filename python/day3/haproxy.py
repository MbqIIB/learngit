#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import os
import time


def ha_display(backend):
    backend_title = 'backend %s' % backend
    server_list = []
    with open('./haproxy.cfg', 'r', encoding="utf-8") as ha_file:
        flag = False       # 这个加得很巧妙,到了下面得if判断中起到了很重要的作用
        for line in ha_file:
            line = line.strip()
            if line == backend_title:  # 如果我找到了用户选择要查看的那个backend
                flag = True            # 标志True,(我找到了)
                continue
            if flag and line.startswith('backend'):  # 到了第二段的backend
                flag = False
                break
            if flag and line.strip():    # 放在第3个if 是前面确认出哪个是用户要的backend,根据flag我这边才打印下面的信息
                server_list.append(line)

    return server_list


def ha_add(backend,server_info=None):
    if server_info == None:
        with open('./haproxy.cfg', 'r', encoding="utf-8") as ha_file:
            backend_title = 'backend %s' % backend
            backend_flag = False
            for line in ha_file:
                if line.strip() == backend_title:
                    backend_flag = True
                    break
            if backend_flag == False:
                ha_file = open('./haproxy.cfg', 'a', encoding="utf-8")
                ha_file.write("\n\n%s\n" % backend_title)
    else:
        with open('./haproxy.cfg', 'r', encoding="utf-8") as ha_file, open('./haproxy.cfg.tmp', 'w', encoding="utf-8") as new_ha_file:
            backend_title = 'backend %s' % backend
            flag = False
            for line in ha_file:
                if line.strip() == backend_title:
                    flag = True
                    new_ha_file.write(line)
                    new_ha_file.write("        %s\n" % server_info)
                    continue
                if flag and line.startswith('backend'):
                    flag = False
                # if flag :
                new_ha_file.write(line)
            os.rename("./haproxy.cfg", "./haproxy.cfg.bak")
            os.rename("./haproxy.cfg.tmp", "./haproxy.cfg")

# ha_add("www.oldboy.org", server_info='server 100.1.7.9 100.1.7.9 weight 20 maxconn 3003')


def ha_remove(backend,server_info=None):
    with open('./haproxy.cfg', 'r', encoding="utf-8") as ha_file, open('./haproxy.cfg.tmp', 'w',encoding="utf-8") as new_ha_file:
    # 先加载到内存中,然后移动文件没关系了.
        os.rename("./haproxy.cfg", "./haproxy.cfg.bak")
        backend_title = 'backend %s' % backend
        flag = False
        if server_info == None:
            for line in ha_file:
                if line.strip() == backend_title:
                    flag = True
                    continue
                if flag and line.startswith('backend'):
                    flag = False
                if flag:
                    continue
                new_ha_file.write(line)
        else:
            for line in ha_file:
                if line.strip() == backend_title:
                    flag = True
                    new_ha_file.write(line)
                    continue
                if flag and line.startswith('backend'):
                    flag = False
                if flag and line.strip() == server_info:
                    continue
                new_ha_file.write(line)
        os.rename("./haproxy.cfg.tmp", "./haproxy.cfg")
    # print("修改完毕,原文件备份为haproxy.cfg.bak")

# ha_remove('www.lianglian.com') #,server_info='server 100.1.7.9 100.1.7.9 weight 20 maxconn 4444')



def ha_update(backend,server_info,new_server_info):
    with open('./haproxy.cfg', 'r', encoding="utf-8") as ha_file, open('./haproxy.cfg.tmp', 'w', encoding="utf-8") as new_ha_file:
        backend_title = 'backend %s' % backend
        flag = False
        for line in ha_file:
            if line.strip() == backend_title:
                flag = True
                new_ha_file.write(line)
                continue
            if flag and line.startswith('backend'):
                flag = False
            if flag and line.strip() == server_info:
                line = line.replace(server_info, new_server_info)
            new_ha_file.write(line)
    os.rename("./haproxy.cfg", "./haproxy.cfg.bak")
    os.rename("./haproxy.cfg.tmp", "./haproxy.cfg")
    # print("修改完毕,原文件备份为haproxy.cfg.bak")

# ha_update('www.oldboy.org', 'server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000',
# 'server 100.1.7.9 100.1.7.9 weight 20 maxconn 3333')


while True:
    print("HAproxy 配置文件修改".center(50,"="))
    print("您可做操作".center(50, "="))
    print("|" + "1.查看".center(50," ") + "|")
    print("|" + "2.修改".center(50," ") + "|")
    print("|" + "3.添加".center(50," ") + "|")
    print("|" + "4.删除".center(50," ") + "|")
    print("|" + "5.退出".center(50," ") + "|")
    print("=".center(54, "="))
    operation_input = input("请输入操作序号:")
    if operation_input == "1":
        backend_name_list = []
        with open("./haproxy.cfg", "r") as ha_file:
            for line in ha_file.readlines():
                if line.startswith("backend"):
                    backend_line = line.split()
                    backend_name_list.append(backend_line[1])  # backend 域名
            for index, backend_name in enumerate(backend_name_list):
                print("\033[;34;0m%d %s\033[0m" % (index, backend_name))
        backend_input = input("请输入要操作的backend序号:")
        backend_name = backend_name_list[int(backend_input)]
        server_info_list = ha_display(backend_name)
        if backend_input.isdigit() and int(backend_input) < len(backend_name_list):
            for index, server_info in enumerate(server_info_list):
                print(index, server_info)
        else:
            print("您的输入有误!")
    elif operation_input == "2":
        backend_name_list = []
        with open("./haproxy.cfg", "r") as ha_file:
            for line in ha_file.readlines():
                if line.startswith("backend"):
                    backend_line = line.split()
                    backend_name_list.append(backend_line[1])  # backend 域名
            for index, backend_name in enumerate(backend_name_list):
                print("\033[;34;0m%d %s\033[0m" % (index, backend_name))
        backend_input = input("请输入要操作的backend序号:")
        backend_name = backend_name_list[int(backend_input)]
        server_info_list = ha_display(backend_name)
        if backend_input.isdigit() and int(backend_input) < len(backend_name_list):
            for index, server_info in enumerate(server_info_list):
                print(index, server_info)
            update_server_info_input = int(input("请输入要操作的server_info的序号:"))
            update_server_info = input("请输入新的内容(按照上面格式写):")
            server_info = server_info_list[update_server_info_input]
            new_server_info = update_server_info
            ha_update(backend_name, server_info, new_server_info)
        else:
            print("您的输入有误!")
    elif operation_input == "3":
        backend_name_list = []
        print("您可做操作".center(50, "="))
        print("|" + "1.添加backend".center(50, " ") + "|")
        print("|" + "2.添加server".center(50, " ") + "|")
        print("|" + "3.返回".center(50, " ") + "|")
        print("|" + "4.退出".center(50, " ") + "|")
        print("=".center(54, "="))
        add_input = input("请输入您所要做的操作:")
        if add_input == '1':
            new_backend = input("请输入backend名称:")
            ha_add(new_backend)
        elif add_input == '2':
            with open("./haproxy.cfg", "r") as ha_file:
                for line in ha_file.readlines():
                    if line.startswith("backend"):
                        backend_line = line.split()
                        backend_name_list.append(backend_line[1])  # backend 域名
                for index, backend_name in enumerate(backend_name_list):
                    print("\033[;34;0m%d %s\033[0m" % (index, backend_name))
            backend_input = int(input("请输入要操作的backend序号:"))
            backend_name = backend_name_list[backend_input]
            new_server_info = input("请输入新的server记录:")
            ha_add(backend_name, server_info=new_server_info)
        elif add_input == '3':
            continue
        elif add_input == '4':
            break
        else:
            print("您的输入有误")

    elif operation_input == "4":
        backend_name_list = []
        with open("./haproxy.cfg", "r") as ha_file:
            for line in ha_file.readlines():
                if line.startswith("backend"):
                    backend_line = line.split()
                    backend_name_list.append(backend_line[1])  # backend 域名
            for index, backend_name in enumerate(backend_name_list):
                print("\033[;34;0m%d %s\033[0m" % (index, backend_name))
        backend_input = input("请输入要操作的backend序号:")
        if backend_input.isdigit() and int(backend_input) < len(backend_name_list):
            backend_name = backend_name_list[int(backend_input)]
            server_info_list = ha_display(backend_name)   # 通过查看得到seveer 配置列表
            print("您可做操作".center(50, "="))
            print("|" + "1.删除backend".center(50, " ") + "|")
            print("|" + "2.删除server".center(50, " ") + "|")
            print("|" + "3.返回".center(50, " ") + "|")
            print("|" + "4.退出".center(50, " ") + "|")
            print("=".center(54, "="))
            remove_input = input("请输入您所要做的操作:")
            if remove_input == '1':
                confirm = input("确定删除整个backend[%s]?(y/n)" % backend_name)
                if confirm == 'y':
                    ha_remove(backend_name)
            elif remove_input == '2':
                for index, server_info in enumerate(server_info_list):
                    print(index, server_info)
                del_server = int(input("请输入你要删除的server序号:"))
                ha_remove(backend_name,server_info_list[del_server])
            elif remove_input == '3':
                continue
            elif remove_input == '4':
                break
            else:
                print("您的输入有误")
        else:
            print("您的输入有误!")
    elif operation_input == "5":
        break
