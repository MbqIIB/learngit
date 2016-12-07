#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# import socketserver
# import subprocess
#
#
# class MyServer(socketserver.BaseRequestHandler):
#
#     def handle(self):  # 定义handle方法
#
#         self.request.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding="utf-8"))  # 发送一个消息
#         while True:
#             data = self.request.recv(1024)
#             if len(data) == 0: break
#             print("[%s] says:%s" % (self.client_address, data.decode()))
#             cmd = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
#             cmd_res = cmd.stdout.read()
#             if not cmd_res:
#                 cmd_res = cmd.stderr.read()
#             if len(cmd_res) == 0:
#                 cmd_res = bytes("cmd has not output", encoding="utf-8")
#
#             self.request.send(cmd_res)
#
# if __name__ == '__main__':
#     server = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)
#     server.serve_forever()
#
#
#
# import socket
# import threading
# import select
#
#
# def process(request, client_address):
#     print(request,client_address)
#     conn = request
#     conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.')
#     flag = True
#     while flag:
#         data = conn.recv(1024)
#         if data == 'exit':
#             flag = False
#         elif data == '0':
#             conn.sendall('通过可能会被录音.balabala一大推')
#         else:
#             conn.sendall('请重新输入.')
#
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.bind(('127.0.0.1', 8002))
# sk.listen(5)
#
# while True:
#     r, w, e = select.select([sk, ], [], [], 1)
#     print('looping')
#     if sk in r:
#         print('get request')
#         request, client_address = sk.accept()
#         t = threading.Thread(target=process, args=(request, client_address))
#         t.daemon = False
#         t.start()
#
# sk.close()



# import socketserver
#
#
# class MyServer(socketserver.BaseRequestHandler):
#
#     def handle(self):
#         conn = self.request  # 接受连接请求,获取客户端socket对象
#         conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.')  # 回一条消息给客户端
#         while True:
#             data = str(conn.recv(1024), encoding='utf-8')
#             # 如果客户端没有输入内容则跳出本次循环什么都不执行
#             if data == len(data):
#                 break
#             # 根据用户输入的内容执行相应的操作
#             elif data == '0':
#                 conn.sendall('通过可能会被录音.balabala一大推')
#             else:
#                 conn.sendall('请重新输入.')
#
#
# if __name__ == '__main__':
#     # 实例话对象,传递一个元祖设置启动的IP/PORT,第二个参数把自己定义的类写上作为SocketServer.ThreadingTCPServer的构造函数
#     server = socketserver.ThreadingTCPServer(('127.0.0.1',8000), MyServer)
#     # 对象调用父类的启动方法
#     server.serve_forever()
#
#
#
#
# import socket
#
#
# ip_port = ('127.0.0.1',8009)
# sk = socket.socket()
# sk.connect(ip_port)
# sk.settimeout(5)
#
# while True:
#     data = sk.recv(1024)
#     print('receive:',data)
#     inp = input('please input:')
#     sk.sendall(inp)
#     if inp == 'exit':
#         break
#
# sk.close()

import socket
import threading
import select


def process(request, client_address):  # 模拟定义的handle()方法，这个方法内的代码是socket server与Client端交互代码
    print(request,client_address)
    conn = request
    conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.')
    flag = True
    while flag:
        data = conn.recv(1024)
        if data == 'exit':
            flag = False
        elif data == '0':
            conn.sendall('通过可能会被录音.balabala一大推')
        else:
            conn.sendall('请重新输入.')


sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 8002))
sk.listen(5)

while True:  # 监控sk文件句柄,循环接受连接请求
    r, w, e = select.select([sk, ], [], [], 1)
    print('looping')
    if sk in r:  # 当sk文件句柄发生变化的时候说明是新的客户端连接过来了
        print('get request')
        request, client_address = sk.accept()
        t = threading.Thread(target=process, args=(request, client_address))  # 创建一个线程，并调用自己定义的process方法执行~然后样客户端与之交互
        t.daemon = False
        t.start()

sk.close()