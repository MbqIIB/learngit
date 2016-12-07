#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('127.0.0.1', 22, 'lianliang', 'woyaojueqi')
# stdin, stdout, stderr = ssh.exec_command('df')
# print(str(stdout.read(), encoding='utf-8'))
# ssh.close();



# import paramiko
#
# private_key_path = '/Users/lianliang/.ssh/id_rsa'
# key = paramiko.RSAKey.from_private_key_file(private_key_path)
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('127.0.0.1 ', 22, 'lianliang', key)
#
# stdin, stdout, stderr = ssh.exec_command('df')
# print(str(stdout.read(), encoding='utf-8'))
# ssh.close()


# import paramiko
#
# t = paramiko.Transport(('127.0.0.1', 22))
# t.connect(username='lianliang', password='123')
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put('/Users/lianliang/PycharmProjects/python_-study/day6/txt', '/root/txt')  # 上传文件,目标路径要写全,写上文件名
# sftp.get('/root/txt', '/Users/lianliang/txt')  # 下载文件.
# t.close()




# import paramiko
#
# pravie_key_path = '/home/auto/.ssh/id_rsa'
# key = paramiko.RSAKey.from_private_key_file(pravie_key_path)
#
# t = paramiko.Transport(('182.92.219.86',22))
# t.connect(username='lianliang', pkey=key)
#
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.put('/tmp/test3.py', '/tmp/test3.py')
# sftp.get('/tmp/test3.py', '/tmp/test3.py')
#
# t.close()
