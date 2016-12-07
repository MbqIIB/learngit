#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import socket
ip_port = ('127.0.0.1',9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sk.bind(ip_port)

while True:
    data = sk.recv(1024)
    print(str(data, encoding='utf-8'))