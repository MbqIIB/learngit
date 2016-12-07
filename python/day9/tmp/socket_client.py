#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import socket

ip_port = ('127.0.0.1', 8888)

sk = socket.socket()   # 创建套接字
sk.connect(ip_port)    # 绑定端口和IP

sk.sendall(bytes('请求占领地球', encoding='utf-8'))   # 发送消息3.x只能发送bytes,2.x能发送str

server_reply = sk.recv(1024)       # 接收数据(1024大小数据(字符))
print(str(server_reply, encoding='utf-8'))  # 由于client &    Server之前传输的是bytes类型,输出要转换成str类型

sk.close()