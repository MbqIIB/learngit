#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5


import paramiko
import uuid

class SSHConnection(object):

    def __init__(self, host='192.168.11.61', port=22, username='alex',pwd='alex3714'):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__k = None

    def run(self):
        self.connect()
        pass
        self.close()

    def connect(self):
        transport = paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def cmd(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        # 执行命令
        stdin, stdout, stderr = ssh.exec_command(command)
        # 获取命令结果
        result = stdout.read()
        return result

    def upload(self,local_path, target_path):
        # 连接，上传
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

ssh = SSHConnection()
ssh.connect()

r1 = ssh.cmd('df')
print(r1)

ssh.upload('/Users/lianliang/ecto.zip', "/home/alex/test7.py")

ssh.close()