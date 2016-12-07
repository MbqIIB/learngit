#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5
# from multiprocessing import Pool
# import time
#
# def f1(arg):
#     time.sleep(1)
#     print(arg)
#
# if __name__ == '__main__':
#     pool = Pool(5)
#     for i in range(30):
#         pool.apply(func=f1, args=(i, ))
#         # pool.apply_async(func=f1, args=(i, ))
#
#     # pool.terminate()  # 立即结束
#     pool.close()        # 所有子进程执行完毕
#     pool.join()


from multiprocessing import Process, Pool
import time


def Foo(i):
    time.sleep(2)
    return i+100


def Bar(arg):
    print(arg)

pool = Pool(5)  # 创建一个进程池
# print(pool.apply(Foo,(1,)))  #去进程池里去申请一个进程去执行Foo方法
# print(pool.apply_async(func=Foo, args=(1,)).get())  # 同上一个意思

for i in range(10):
    # print(pool.apply(Foo, (i,)))
    pool.apply_async(func=Foo, args=(i,),callback=Bar)

print('end')
pool.close()
# pool.terminate()  # 立即结束
pool.join()  # 主进程等待进程池中子进程执行完毕后再关闭，如果注释，那么程序直接关闭。

'''
pool.apply 主动的去执行
pool.apply_async(func=Foo, args=(i,),callback=Bar) 相当于异步，当申请一个线程之后，执行FOO方法就不管了，执行完之后就再执行callback ，当你执行完之后，再执行一个方法告诉我执行完了
callback 有个函数，这个函数就是操作的Foo函数的返回值！
'''