#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8888,))
data = sk.recv(1024)
print(data)
while True:
    inp = input(">>>")
    sk.sendall(bytes(inp,encoding='utf-8'))
    print(sk.recv(1024))
sk.close()