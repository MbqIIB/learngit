#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import socket
ip_port = ('127.0.0.1',9999)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
while True:
    inp = bytes(input('数据：').strip(), encoding='utf-8')
    if inp == 'exit':
        break
    sk.sendto(inp, ip_port)

sk.close()