#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import json
import socket
import subprocess

ip_port = ('127.0.0.1', 8000)
# 创建socket对象
s = socket.socket()
# 侦听的IP和端口
s.bind(ip_port)
# 设置client最大等待连接数,最多等待五个连接,其他的直接报错
s.listen(5)
while True:  # 循环

    # 只有accept & recv 会阻塞，这里accept阻塞，直到有client连接过来
    # accept()接受客户端发送过来的请求:connection代表客户端对象，address是客户端的IP
    connection, address = s.accept()

    while True:
        try:
            # recv()接收客户端信息
            recv_data = connection.recv(1024)

            # 如果为空则退出这层循环,不做操作
            if not recv_data:
                break

            # 接收到client端发送过来的指令并执行
            p = subprocess.Popen(str(recv_data, encoding='utf-8'), shell=True, stdout=subprocess.PIPE)
            # 获取命令输出结果
            res = p.stdout.read()
            if res:
                send_data = str(res, encoding='utf-8')
            else:
                send_data = 'cmd error'

            # str转换bytes
            send_data = bytes(send_data, encoding='utf-8')

            # 发送准备就绪和准备要发送的内容长度,防止粘包(发送内容超出接收端内容,多出的内容出现在下一次接收得内容中)
            '''
            粘包: 命令执行结果返回字符串长度为2018,如果客户端只接受1024,就接受了一次,那么多出来的内容回去哪呢,
                  多出来的内容会出现在下一次返回前头,这就是粘包(分包传递,内容接收端发生错误)
            '''
            # 讲要发送的内容信息json格式发送客户端,客户端好做好准备接收
            ready_dict = {'status': 'Ready',
                          'msg_size': len(send_data),}
            ready_tag = json.dumps(ready_dict)
            connection.send(bytes(ready_tag, encoding='utf-8'))

            # 等待client 'Start'信号后开始
            feedback = connection.recv(1024)   # Start
            feedback = str(feedback, encoding='utf-8')
            if feedback == 'Start':
                # 发送指令返回结果的内容
                connection.send(send_data)

        except Exception:
            break

    # 关闭和client的连接
    connection.close()


