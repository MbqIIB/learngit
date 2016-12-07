#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5
import queue
import threading
import time

q = queue.Queue()

# 生成者(client)
def productor(arg):
    # 序号加包子,将做好的包子放到篮子(队列)里
    q.put(str(arg) + '包子')

# 创建30个包子
for i in range(30):
    t = threading.Thread(target=productor, args=(i,))
    t.start()

# ============================================================== #

# 消费者(server)
def consumer(arg):
    while True:
        # arg(0-3)吃包子得人, q.get()从篮子(队列)里取包子,包子有序号
        print(arg, q.get())
        time.sleep(2)

# 三个线程一起吃包子
for j in range(3):
    t = threading.Thread(target=consumer, args=(j,))
    t.start()