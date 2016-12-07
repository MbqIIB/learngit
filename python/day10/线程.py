#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

def f1(arg):
    print(arg)


import threading
t = threading.Thread(target=f1, args=(123,))
t.start()
# t.setDaemon(True)  # True ,表示主线程不等此子线程
t.join(2)          # 表示主线程到此,等待..
                   # 参数,表示主线程在此最多等待N秒
f1(111)
print("end")
print("end")
print("end")
print("end")
print("end")
print("end")



# import threading
# import time
#
# def show(arg):
#     time.sleep(1)
#     print('thread'+str(arg))
#
# for i in range(10):
#     t = threading.Thread(target=show, args=(i,))
#     t.start()
#
# print('main thread stop')