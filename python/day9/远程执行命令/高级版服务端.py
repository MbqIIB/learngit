# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author: Liang Lian
# # Python 3.5

import socket
import select
import queue
import subprocess
import json
sk = socket.socket()  # 创建socket对象
sk.bind(('127.0.0.1', 6666,))  # 设置监听的IP与端口
sk.listen(5)  # 设置client最大等待连接数
inputs = [sk, ]  # 需要侦听接收消息的socket对象列表
outputs = []  # 所有给server端发过消息的客户端socket列表,都是需要回消息的
messages = {}  # 接受到的消息
# message的样板信息
# message = {
#    'c1':队列(存放客户端发送过来的消息)
#    'c2':队列，
# }

while True:  # 循环
    rlist, wlist, e = select.select(inputs, outputs, [], 1)
    meu = '''
    inputs(侦听已经链接的socket列表): %s
    rlist(侦听的socket中发生变化的socket列表): %s
    wlist(侦听回消息列表,发生变化的socket列表): %s
    outputs(需要回消息的socket列表): %s
    '''
    print(meu % (len(inputs), len(rlist), len(wlist), len(outputs)))
    # 监听sk(服务器端)对象,如果sk对象发生变化,表示有客户端连接来了,此时rlist值为[sk]
    # 监听connection对象,如果connection发生变化,表示客户端有新消息发过来了,此时rlist的值为[客户端]
    # rlist = [sk,]
    for r in rlist:  # 轮询侦听的socket列表
        if r == sk:  # 如果侦听到是服务端socket发送变化了,说明有新的客户端链接过来了
            connection, address = r.accept()  # 接收客户端对象
            # connection是什么? 其实是客户端socket对象
            inputs.append(connection)  # 加到侦听的socket对象列表中
            messages[connection] = queue.Queue()  # 字典中为这个客户端连接建立一个消息队列
        else:
            '''
            如果侦听到发送变化的socket对象不是服务端自己的socket,那么就是客户端socket变化了,说明客户端那边发消息过来了
            '''
            # 有人给我发消息了
            print("=======")
            ret = r.recv(1024)  # 接收消息
            if ret:
                p = subprocess.Popen(str(ret, encoding='utf-8'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                res = p.stdout.read()
                if not res:
                    res = 'command error'
                # 解决连包
                msg_size = len(res)
                response_msg = {'status': 'Ready',
                                'size': msg_size,
                                'content': res}
                response_msg = json.dumps(response_msg)
                outputs.append(r)  # 接收完消息后把客户对象加到回消息列表
                messages[r].put(response_msg)  # 把接受到的消息加到字典里面
            else:
                inputs.remove(r)  # 报错,客户端链接断开,删除侦听的客户端socket对象
    # 所有给我发过消息的人
    for w in wlist:
        try:
            msg = messages[w].get_nowait()  # 去指定队列取数据,并且不阻塞
            msg_dict = json.loads(msg)
            w.sendall(bytes(str(msg_dict['size']), encoding='utf-8'))
            recv_tag = w.recv(1024)
            if str(recv_tag, encoding='utf-8') == 'Start':
                response = bytes(msg_dict['content'], encoding='utf-8')
                w.sendall(response)     # 反馈消息
                outputs.remove(w)  # 从回消息列表中删除客户端socket对象
            else:
                raise Exception('断开连接')
        except Exception as error:  # 发送异常,说明连接中断
            del messages[r]  # 删除接收到的消息

# # rlist = [sk,], rlist=[sk1,],rlist=[sk1,sk2]
# # rlist = []



# import select
# import socket
# import queue
# import time
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',6666))
# sk.listen(5)
# sk.setblocking(False) #定义非阻塞
# inputs = [sk,]  #定义一个列表，select第一个参数监听句柄序列,当有变动是，捕获并把socket server加入到句柄序列中
# outputs = [] #定义一个列表，select第二个参数监听句柄序列，当有值时就捕获，并加入到句柄序列
# message = {}
# #message的样板信息
# #message = {
# #    'c1':队列，[这里存放着用户C1发过来的消息]例如:[message1,message2]
# #    'c2':队列，[这里存放着用户C2发过来的消息]例如:[message1,message2]
# #}
#
#
# while True:
#     readable_list, writeable_list, error_list = select.select(inputs,outputs,[],1)
#     #文件描述符可读 readable_list    只有第一个参数变化时候才捕获，并赋值给readable_list
#     #文件描述符可写 writeable_list   只要有值，第二个参数就捕获并赋值给writeable_list
#     #time.sleep(2)
#     print('inputs:',inputs)
#     print('output:')
#     print('readable_list:',readable_list)
#     print('writeable_list:',writeable_list)
#     print('message',message)
#     for r in readable_list: #当readable_list有值得时候循环
#         if r == sk:  #判断是否为链接请求变化的是否是socket server
#             conn,addr = r.accept() #获取请求
#             inputs.append(conn) #把客户端对象（句柄）加入到inputs里
#             message[conn] = queue.Queue() #并在字典里为这个客户端连接建立一个消息队列
#         else:
#             client_data = r.recv(1024) #如果请求的不是sk是客户端接收消息
#             if client_data:#如果有数据
#                 outputs.append(r)#把用户加入到outpus里触发select第二个参数
#                 message[r].put(client_data)#在指定队列中插入数据
#             else:
#                 inputs.remove(r)#没有数据，删除监听链接
#                 del message[r] #当数据为空的时候删除队列~~
#     for w in writeable_list:#如果第二个参数有数据
#         try:
#             data = message[w].get_nowait()#去指定队列取数据 并且不阻塞
#             w.sendall(data) #返回请求输入给client端
#         except queue.Empty:#反之触发异常
#             pass
#         outputs.remove(w) #因为第二个参数有值得时候就触发捕获值，所以使用完之后需要移除它
#         #del message[r]
#     print('%s' %('-' * 40))