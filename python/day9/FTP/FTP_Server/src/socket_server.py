#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import os
import re
import sys
import json
import getpass
import socketserver


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.utils import Config, md5
from src.user import AdminUser

# 读取配置文件
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'etc', 'config.ini')
CONFIG = Config(config_path, section='SERVER')
# 调用管理用户的类
admin_user = AdminUser()


class MyServer(socketserver.BaseRequestHandler, AdminUser):

    user_json = json.load(open(os.path.join(CONFIG.db_path, 'user.json'), 'r'))
    user_name = None
    user_path = None
    current_path = None

    def handle(self):
        while True:
            try:
                command_str = str(self.request.recv(1024), encoding='utf-8')
                if len(command_str) == 0:
                    break
                else:
                    self.cmd(command_str)
            except Exception as error:
                print('Error: %s' % error)
                break

    def cmd(self, command_str):
        """
        命令字典反射
        :param command_str:
        :return:
        """
        # client 传递的命名字符串做解析
        command_dict = json.loads(command_str)
        # 获取用户命令主键
        command = command_dict['command']
        # 通过反射调用对应方法
        if hasattr(self, command):
            func = getattr(self, command)
            func(command_dict)
            return True

    def _new_path(self, path):
        # 真实路径转客户端看到的路径
        if path.startswith(self.user_path):
            path = re.sub(self.user_path, '', path)
            return path
        # 客户端路径转真实路径
        if path.startswith('/'):
            path = os.path.join(self.user_path, re.sub('/', '', path, 1))
            return path
        path = os.path.join(self.current_path, path)
        return path

    def _get_size(self, file_path):
        """
        计算文件或目录大小
        :param file_path:
        :return:
        """
        if not os.path.exists(file_path):
            return 0

        if os.path.isfile(file_path):
            return os.path.getsize(file_path)

        size = 0
        for root, dirs, files in os.walk(file_path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size

    def login(self, command_dict):
        """
        用户登录
        :param command_dict:
        :return:
        """
        user = command_dict['user_name']
        password = command_dict['password']
        if admin_user.login(user, password):
            self.user_name = user
            self.user_path = os.path.join(CONFIG.data_path, user)
            self.current_path = self.user_path
            self.request.sendall(bytes('Login successful.', encoding='utf-8'))
        else:
            self.request.sendall(bytes('Login fail.', encoding='utf-8'))

    def ls(self, command_dict):
        """
        查看命令
        :param command_dict:
        :return:
        """

        # 切换路径
        if command_dict.get('file_path'):
            dir_path = command_dict['file_path']
            dir_path = self._new_path(dir_path)
            # 判断用户查看的是否是目录
            if not os.path.isdir(dir_path):
                # 用户查看的路径不是目录
                self.request.sendall(bytes('Error: Command ls fail: Path is not directory', encoding='utf-8'))
                return False
            # 获取当前路径下文件目录
        else:
            dir_path = self.current_path
        dir_list = os.listdir(dir_path)
        # 如果是目录则将名字变成蓝色
        file_list = []
        for file in dir_list:
            file_path = os.path.join(dir_path, file)
            # 判断是否是目录
            if os.path.isdir(file_path):
                # 将目录的字符串加蓝色显示,去掉换行
                file_name = re.split('\n', file)[0]
                file = re.sub(file_name, '\033[34;0m{file}\033[0m'.format(file=file_name), file_name)
                file_list.append(file)
                continue
            file_list.append(file)
        file_list_str = json.dumps(file_list)
        cmd_length = len(bytes(file_list_str, encoding='utf-8'))
        cmd_dict = {'cmd_length': cmd_length, }
        cmd_msg = json.dumps(cmd_dict)
        self.request.sendall(bytes(cmd_msg, encoding='utf-8'))

        # 接收客户端答复
        status = self.request.recv(1024)
        status = str(status, encoding='utf-8')
        if status == 'start':
            self.request.sendall(bytes(file_list_str, encoding='utf-8'))
        else:
            self.request.sendall(bytes('Command not run!', encoding='utf-8'))

    def mkdir(self, command_dict):
        """
        创建目录
        :param command_dict:
        :return:
        """
        path = command_dict['dir_path']
        dir_path = self._new_path(path)
        # 判断目录是否存在
        if os.path.exists(dir_path):
            self.request.sendall(bytes('Command mkdir fail: Directory already exists', encoding='utf-8'))
            return False

        os.makedirs(dir_path)
        # 判断创建是否成功
        if os.path.isdir(dir_path):
            self.request.sendall(bytes('Directory to create success', encoding='utf-8'))
            return True

    def remove(self, command_dict):
        """
        删除命令
        :param command_dict:
        :return:
        """
        path = command_dict['file_path']
        file_path = self._new_path(path)
        # 判断目录是否存在
        if not os.path.exists(file_path):
            self.request.sendall(bytes('Command remove fail,No such file or directory', encoding='utf-8'))
            return False

        if os.path.isdir(file_path):
            try:
                os.rmdir(file_path)
                self.request.sendall(bytes('Command remove success', encoding='utf-8'))
            except Exception as error:
                self.request.sendall(bytes('Command remove fail,The directory is not empty', encoding='utf-8'))
        else:
            try:
                os.remove(file_path)
                self.request.sendall(bytes('Command remove success', encoding='utf-8'))
            except Exception as error:
                self.request.sendall(bytes('Command remove fail,%s' % error, encoding='utf-8'))

    def cd(self, command_dict):
        """
        切换目录
        :param command_dict:
        :return:
        """
        # 用户是否给路径
        if not command_dict.get('dir_path'):
            self.current_path = self.user_path
            self.request.sendall(bytes('Command cd success', encoding='utf-8'))
            return True

        # 用户可切换的目录
        dir_list = []
        for root, dir, files in os.walk(self.user_path):
                dir_list.append(root)

        dir = command_dict['dir_path']
        user_path = self._new_path(dir)
        if dir == '/':
            self.current_path = self.user_path
            self.request.sendall(bytes('Command cd success', encoding='utf-8'))
            return True
        print(user_path)
        # 判断目录是否在用户家目录中
        if user_path not in dir_list:
            self.request.sendall(bytes('Command cd: no such directory', encoding='utf-8'))
            return False
        else:
            self.current_path = user_path
            self.request.sendall(bytes('Command cd success', encoding='utf-8'))

    def pwd(self, command_dict):
        """
        查看当前目录
        """
        if self.current_path == self.user_path:
            pwd = '/'
        else:
            pwd = self._new_path(self.current_path)
        self.request.sendall(bytes(pwd, encoding='utf-8'))

    def du(self, command_dict):
        """
        统计大小
        :param command_dict:
        :return:
        """
        file_path = self.current_path

        if command_dict.get('file_path'):
            path = command_dict['file_path']
            # 客户端路径转真实路径
            file_path = self._new_path(path)

        file_size = self._get_size(file_path)
        # 真实路径转客户端路径
        file_path = self._new_path(file_path)
        if file_size < 1024:
            self.request.sendall(bytes('Size: %s [%.3f B]' % (file_path, file_size), encoding='utf-8'))
        elif 1024 * 1024 > file_size > 1024:
            file_size /= 1024
            self.request.sendall(bytes('Size: %s [%.3f KB]' % (file_path, file_size), encoding='utf-8'))
        elif 1024 * 1024 * 1024 > file_size > 1024 * 1024:
            file_size /= 1024 * 1024
            self.request.sendall(bytes('Size: %s [%.3f MB]' % (file_path, file_size), encoding='utf-8'))
        elif file_size > 1024 * 1024 * 1024:
            file_size /= 1024 * 1024 * 1024
            self.request.sendall(bytes('Size: %s [%.3f GB]' % (file_path, file_size), encoding='utf-8'))

    def put(self, command_dict):
        """
        上传文件
        :param command_dict:
        :return:
        """
        print(command_dict)
        file_name = command_dict['file_name']
        file_size = command_dict['file_size']
        file_md5 = command_dict['file_md5']
        # 获取用户配额
        user_size = self.user_json[self.user_name]['dir_size']
        # 用户配额减去现使用空间
        user_du = self._get_size(self.user_path)
        user_size -= user_du
        # 判断文件大小是否满足用户空间
        if file_size > user_size:
            self.request.sendall(bytes('Put File Is greater than the user space!', encoding='utf-8'))
            return False
        # 判断客户端是否传路径
        if command_dict.get('file_path'):
            path = command_dict['file_path']
            file_path = os.path.join(self._new_path(path), file_name)
        else:
            file_path = os.path.join(self.current_path, file_name)
        # 判断文件是否存在
        if os.path.exists(file_path):
            des_md5 = md5(str(os.stat(file_path).st_size))
            # 长传文件和原文件一摸一样不上传
            if des_md5 == file_md5:
                self.request.sendall(bytes('Put File to same file name', encoding='utf-8'))
                return False
            # 文件存在,断点续传
            start_tag = 'Put file continue'
            self.request.sendall(bytes(start_tag, encoding='utf-8'))
            continue_length = os.stat(file_path).st_size
            send_length = str(continue_length)
            # 发送server端存在的文件大小,client端从相应地点传
            self.request.sendall(bytes(send_length, encoding='utf-8'))
            # 接受的bytes(字节),追加写'ab'
            try:
                with open(file_path, 'ab') as file:
                    # 从现有文件大小到client端原文件大小一直接收
                    while continue_length < file_size:
                        recv_data = self.request.recv(1024)
                        file.write(recv_data)
                        continue_length += len(recv_data)
            except:
                print("传输文件中断")
        else:
            # 发送消息给客户端,可以开始上传
            start_tag = 'Put File Start'
            self.request.sendall(bytes(start_tag, encoding='utf-8'))
            recv_size = 0
            try:
                with open(file_path, 'wb') as file:
                    while recv_size < file_size:
                        recv_data = self.request.recv(1024)
                        file.write(recv_data)
                        recv_size += len(recv_data)
            except:
                print("传输文件中断")
        # 最后校验文件md5值判断是否上传成功
        des_md5 = md5(str(os.stat(file_path).st_size))
        if des_md5 == file_md5:
            self.request.sendall(bytes('Put File Complete!', encoding='utf-8'))
        else:
            self.request.sendall(bytes('Put File Error!', encoding='utf-8'))

    def get(self, command_dict):
        """
        下载文件
        :param command_dict:
        :return:
        """
        file_name = command_dict['file_name']
        # 查看的当前路径加用户给的文件路径做拼接
        file_path = self._new_path(file_name)

        if not os.path.exists(file_path):
            self.request.sendall(bytes('Error: File not exists', encoding='utf-8'))
            return False
        # 通过接受的文件名获取文件信息
        file_size = os.stat(file_path).st_size
        file_md5 = md5(str(file_size))
        file_name = os.path.basename(file_path)
        file_status = {'file_name': file_name,
                       'file_size': file_size,
                       'file_md5': file_md5}
        # 将文件信息传给客户端
        file_status = json.dumps(file_status)
        self.request.sendall(bytes(file_status, encoding='utf-8'))
        # 接受客户端接下来反馈
        recv_status = self.request.recv(1024)
        # 收到客户端开始传输消息
        if str(recv_status, encoding='utf-8') == 'Get file start':
            try:
                with open(file_path, 'rb') as file:
                    for line in file:
                        self.request.sendall(line)
            except:
                print("传输文件中断")
        # 收到客户端继续传输消息
        elif str(recv_status, encoding='utf-8') == 'Get file continue':
            # 接收用户继续传得点
            continue_length = self.request.recv(1024)
            continue_length = int(str(continue_length, encoding='utf-8'))
            try:
                with open(file_path, 'rb') as file:
                    # 移动文件指针,到继续传输得点
                    file.seek(continue_length)
                    for line in file:
                        self.request.sendall(line)
            except:
                print("传输文件中断")


if __name__ == '__main__':
    run = socketserver.ThreadingTCPServer((CONFIG.listen, int(CONFIG.port)), MyServer)
    run.serve_forever()
