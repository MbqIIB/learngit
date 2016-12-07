#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import threading

# def f1(arg):
#     print(arg)
#
#
# t = threading.Thread(target=f1, args=(123,))
# t.start()



# 自己创建一个线程类,继承threading.Thread类, 重写run方法,start()方法调用内部run()方法
class MyThread(threading.Thread):

    # 初始化接受两个参数
    def __init__(self, func, args):
        self.func = func
        self.args = args

        # super主动调用父类__init__()方法
        super(MyThread, self).__init__()

    # 执行start()方法,我继承类Thread类,它会调用自己的run方法,
    # 我重写了run方法,根据类的继承关系,执行方法现找自己,如果自己有则我自己写的run方法
    def run(self):
        self.func(self.args)


def f2(arg):
    print(arg)


for i in range(10):
    obj = MyThread(f2, i)
    obj.start()




# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self,num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):#定义每个线程要运行的函数
#
#         print("running on number:%s" %self.num)
#
#         time.sleep(3)
#
# if __name__ == '__main__':
#
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()