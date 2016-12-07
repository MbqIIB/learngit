#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


import socket
import select


sk = socket.socket()
sk.bind(('127.0.0.1', 8888,))
sk.listen(5)


inputs = [sk,]
outputs = []
messages = {}
while True:
    rlist,wlist,e = select.select(inputs, outputs, [], 1)
    print(len(inputs),len(rlist),len(wlist),len(outputs))
    # 监听sk(服务器端)对象,如果sk对象发生变化,表示有客户端连接来了,此时rlist值为[sk]
    # 监听conn对象,如果conn发生变化,表示客户端有新消息发过来了,此时rlist的之为[客户端]
    # rlist = [sk,]
    for r in rlist:
        if r == sk:
            # 新客户来连接
            conn, address = r.accept()
            # conn是什么? 其实socket对象
            inputs.append(conn)
            messages[conn] = []
            print(messages)
            conn.sendall(bytes('hello', encoding='utf-8'))
        else:
            # 有人给我发消息了
            print("=======")
            try:
                ret = r.recv(1024)
                if not ret:
                    raise Exception('断开连接')
                else:
                    outputs.append(r)
                    messages[r].append(ret)
            except Exception as e:
                inputs.remove(r)
                del messages[r]
    # 所有给我发过消息的人
    for w in wlist:
        msg = messages[w].pop()
        resp = msg + bytes('response', encoding='utf-8')
        w.sendall(resp)
        outputs.remove(w)


# rlist = [sk,], rlist=[sk1,],rlist=[sk1,sk2]
# rlist = []

