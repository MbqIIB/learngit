#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import socket

ip_port = ('127.0.0.1', 8888)

sk = socket.socket()  # 创建套接字
sk.bind(ip_port)      # 绑定端口和IP
sk.listen(5)          # 设置线程池(最大可接受挂起的请求连接数)

while True:
    print('server waiting...')
    conn, addr = sk.accept()     # 接收的连接和请求的IP & 端口(tuple)

    client_data = conn.recv(1024)   # 用建立的连接操作,接收数据(1024大小数据(字符))
    print(str(client_data, encoding='utf-8'))
    conn.sendall(bytes('僵尸吃了你的脑子!!!', encoding='utf-8'))   # 发送消息3.x只能发送bytes,2.x能发送str

    conn.close()