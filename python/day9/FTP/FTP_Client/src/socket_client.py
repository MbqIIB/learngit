#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import os
import sys
import json
import socket
import getpass

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.utils import md5
from lib.utils import ProgressBar


class Client:

    def __init__(self, ip, port):
        self.host = ip
        self.port = port
        self.user_name = None
        self.sk = socket.socket()
        self.ProgressBar = ProgressBar()

    def mian(self):
        """
        反射调用方法
        :return:
        """
        if self.login():
            while True:
                command = input('ftp>')
                if len(command) == 0:
                    continue
                elif command == "exit":
                    break
                cmd = command.split()[0]
                if hasattr(self, cmd):
                    run = getattr(self, cmd)
                    run(command)
                else:
                    print("指令不对,请help查看帮助信息")

    def login(self):
        """
        用户登录
        :return:
        """
        print('Connected to %s' % self.host)
        user_name = input('UserName:')
        password = getpass.getpass('Password:')
        login_dict = {'command': 'login',
                      'user_name': user_name,
                      'password': md5(password)
                      }
        self.user_name = user_name
        login_info = json.dumps(login_dict)
        self.sk.connect((self.host, self.port))
        self.sk.sendall(bytes(login_info, encoding='utf-8'))

        login_status = self.sk.recv(1024)
        login_status = str(login_status, encoding='utf-8')
        print(login_status)
        if login_status == 'Login successful.':
            return True
        return False

    def ls(self, command_str=None):
        """
        查看目录
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        command_dict = {'command': 'ls',
                        }
        if len(command_list) == 2:
            command_dict['file_path'] = command_list[1]

        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        # 接受命令执行结果
        cmd_status = self.sk.recv(1024)
        cmd_status = str(cmd_status, encoding='utf-8')
        if cmd_status.startswith('Error'):
            print(cmd_status)
            return False

        cmd_status = json.loads(cmd_status)
        str_length = cmd_status['cmd_length']
        if str_length:
            self.sk.sendall(bytes('start', encoding='utf-8'))
        else:
            print("Command Error")
            return False

        recv_size = 0
        recv_msg = b''
        while recv_size < str_length:
            recv_data = self.sk.recv(1024)
            recv_msg += recv_data
            recv_size += len(recv_data)
        file_list = json.loads(str(recv_msg, encoding='utf-8'))
        p_str = ''
        for file in file_list:
            p_str += '{}\t\t\t\t'.format(file)
        print(p_str)

    def mkdir(self, command_str=None):
        """
        创建目录
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        dir_path = command_list[1]
        command_dict = {'command': 'mkdir',
                        'dir_path': dir_path,
                        }
        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        # 接受命令执行结果
        cmd_result = self.sk.recv(1024)
        cmd_result = str(cmd_result, encoding='utf-8')
        if cmd_result.startswith('Error'):
            print(cmd_result)
            return False

        print(cmd_result)

    def remove(self, command_str=None):
        """
        删除操作
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        file_path = command_list[1]
        command_dict = {'command': 'remove',
                        'file_path': file_path,
                        }
        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        # 接受命令执行结果
        cmd_result = self.sk.recv(1024)
        cmd_result = str(cmd_result, encoding='utf-8')
        if cmd_result.startswith('Error'):
            print(cmd_result)
            return False

        print(cmd_result)

    def cd(self, command_str=None):
        """
        切换目录
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        command_dict = {'command': 'cd'}
        if len(command_list) == 2:
            dir_path = command_list[1]
            command_dict['dir_path'] = dir_path
        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        # 接受命令执行结果
        cmd_result = self.sk.recv(1024)
        cmd_result = str(cmd_result, encoding='utf-8')
        if cmd_result.startswith('Error'):
            print(cmd_result)
            return False

        if cmd_result == 'Command cd success':
            return True

    def du(self, command_str=None):
        """
        查看文件大小
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        command_dict = {'command': 'du'}
        if len(command_list) == 2:
            file_path = command_list[1]
            command_dict['file_path'] = file_path

        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        # 接受命令执行结果
        cmd_result = self.sk.recv(1024)
        cmd_result = str(cmd_result, encoding='utf-8')
        if cmd_result.startswith('Error'):
            print(cmd_result)
            return False

        print(cmd_result)

    def pwd(self, command_str=None):
        """
        查看当前所在位置
        :param command_str:
        :return:
        """
        command_dict = {'command': 'pwd'}

        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        # 接受命令执行结果
        cmd_result = self.sk.recv(1024)
        cmd_result = str(cmd_result, encoding='utf-8')
        if cmd_result.startswith('Error'):
            print(cmd_result)
            return False

        print(cmd_result)

    def help(self, command_str=None):
        help_menu = '''
        [帮助信息]
        put         上传文件
        get         下载文件
        ls          查看文件
        pwd         查看当前所在目录
        cd          切换当前目录
        du          统计文件大小
        mkdir       创建目录
        remove      删除
        help        查看帮助信息
        '''

    def put(self, command_str):
        """
        上传文件
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        file = command_list[1]
        file_size = os.stat(file).st_size
        file_md5 = md5(str(file_size))
        file_name = os.path.basename(file)
        # 将命令信息汇总字典
        command_dict = {'command': 'put',
                        'file_name': file_name,
                        'file_size': file_size,
                        'file_md5': file_md5}
        # 路径可传参数
        if len(command_list) == 3:
            file_path = command_list[2]
            command_dict['file_path'] = file_path

        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        feedback = self.sk.recv(1024)  # Put File Start
        feedback = str(feedback, encoding='utf-8')
        if feedback == 'Put File Start':
            print(feedback + '\n')
            try:
                with open(file, 'rb') as f:
                    send_size = 0
                    for line in f:
                        self.sk.sendall(line)
                        send_size += len(line)
                        self.ProgressBar.update(send_size, file_size)
            except:
                print("传输文件中断")
        elif feedback == 'Put file continue':
            print(feedback + '\n')
            continue_length = self.sk.recv(1024)
            continue_length = int(str(continue_length, encoding='utf-8'))
            try:
                with open(file, 'rb') as f:
                    f.seek(continue_length)
                    send_size = continue_length
                    for line in f:
                        self.sk.sendall(line)
                        send_size += len(line)
                        self.ProgressBar.update(send_size, file_size)
            except:
                print("传输文件中断")
        else:
            print(feedback)
            return

        # 接受put文件结果
        result = self.sk.recv(1024)
        print(str(result, encoding='utf-8'))

    def get(self, command_str):
        """
        下载文件
        :param command_str:
        :return:
        """
        command_list = command_str.split()
        file_name = command_list[1]
        des_path = os.path.abspath(os.path.curdir)
        command_dict = {'command': 'get',
                        'file_name': file_name,
                        }

        if len(command_list) == 3:
            des_path = command_list[2]
            if not os.path.isdir(des_path):
                print("目标路径不是目录")
                return False

        command_msg = json.dumps(command_dict)
        self.sk.sendall(bytes(command_msg, encoding='utf-8'))

        file_status = self.sk.recv(1024)
        file_status = str(file_status, encoding='utf-8')
        if file_status.startswith('Error'):
            print(file_status)
            return False

        file_status = json.loads(file_status)
        file_name = file_status['file_name']
        file_path = os.path.join(des_path, file_name)
        file_size = file_status['file_size']
        file_md5 = file_status['file_md5']

        if os.path.exists(file_path):
            if md5(str(os.stat(file_path).st_size)) == file_md5:
                print('File already exists')
                return False

            self.sk.sendall(bytes('Get file continue', encoding='utf-8'))
            recv_size = os.stat(file_path).st_size
            continue_length = str(recv_size)
            self.sk.sendall(bytes(continue_length, encoding='utf-8'))
            try:
                with open(file_path, 'ab') as file:
                    while recv_size < file_size:
                        recv_data = self.sk.recv(1024)
                        file.write(recv_data)
                        recv_size += len(recv_data)
                        self.ProgressBar.update(recv_size, file_size)
                return True
            except Exception as error:
                print('Get file fail: %s' % error)
        self.sk.sendall(bytes('Get file start', encoding='utf-8'))
        recv_size = 0
        try:
            with open(file_path, 'wb') as file:
                while recv_size < file_size:
                    recv_data = self.sk.recv(1024)
                    file.write(recv_data)
                    recv_size += len(recv_data)
                    self.ProgressBar.update(recv_size, file_size)
        except Exception as error:
            print('Get file fail: %s' % error)

        if md5(str(os.stat(file_path).st_size)) == file_md5:
            print('Get File Complete!')
            # os.remove(file_path)
            return True

if __name__ == '__main__':
    # host, port = (sys.argv[1], int(sys.argv[2]))
    host, port = ('127.0.0.1', 8888)  # IDE调试
    obj = Client(host, port)
    obj.mian()

