#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# # 创建进程
# from multiprocessing import Process
#
#
# def foo(i):
#     print('say hi',i)
#
# for i in range(10):
#     p = Process(target=foo,args=(i,))
#     p.start()


# # 进程间默认无法数据共享
# from multiprocessing import Process
#
# li = []
#
#
# def foo(i):
#     li.append(i)
#     print('say hi', li)
#
# for i in range(10):
#     p = Process(target=foo, args=(i,))
#     p.start()
#
# # 进程中数据不共享,这里主进程的li列表中还是空
# print('ending', li)


# # 方法一，Array
# from multiprocessing import Process, Array
# # 定义数组
# temp = Array('i', [11, 22, 33, 44])
#
#
# def Foo(i):
#     temp[i] = 100+i
#     for item in temp:
#         # 打印子进程中得value
#         print(i, '----->', item)
#
# for i in range(2):
#     p = Process(target=Foo, args=(i,))
#     p.start()
#
#
# # # 方法二：manage.dict()共享数据
# from multiprocessing import Process, Manager
#
# manage = Manager()
# dic = manage.dict()
#
#
# def Foo(i):
#     dic[i] = 100+i
#     print(dic.values())
#
# for i in range(10):
#     p = Process(target=Foo, args=(i,))
#     p.start()
#     p.join()



# from multiprocessing import Process, Queue
#
#
# def f(i,q):
#     print(i, q.get())
#
# if __name__ == '__main__':
#     q = Queue()
#     q.put("h1")
#     q.put("h2")
#     q.put("h3")
#
#     for i in range(10):
#         p = Process(target=f, args=(i, q,))
#         p.start()



# # 进程锁
# from multiprocessing import Process, Array, RLock
#
#
# def Foo(lock, temp, i):
#     """
#     将第0个数加100
#     """
#     lock.acquire()
#     temp[0] += 100
#     for item in temp:
#         print(i, '----->', item)
#     lock.release()
#
# lock = RLock()
# temp = Array('i', [11, 22, 33, 44])
#
# for i in range(10):
#     p = Process(target=Foo,args=(lock, temp, i,))
#     p.start()


# from multiprocessing import Process, Pool
# import time
#
#
# def Foo(i):
#     time.sleep(2)
#     return i+100
#
#
# def Bar(arg):
#     print(arg)
#
# pool = Pool(5)
# # print(pool.apply(Foo,(1,)))
# # print(pool.apply_async(func =Foo, args=(1,)).get())
#
# for i in range(10):
#     pool.apply_async(func=Foo, args=(i,),callback=Bar)
#
# print('end')
# pool.close()
# pool.join()  # 主进程等待进程池中子进程执行完毕后再关闭，如果注释，那么程序直接关闭。




# from multiprocessing import Process
# from multiprocessing import queues
# import multiprocessing
#
#
# def foo(i, arg):
#     arg.put(i)
#     print('say hi', i, arg.qsize())
#
#
# if __name__ == '__main__':
#     li = queues.Queue(20, ctx=multiprocessing)
#     for i in range(10):
#         p = Process(target=foo, args=(i, li, ))
#         # p.daemon = True
#         p.start()
#         p.join()





# from multiprocessing import Process
# from multiprocessing import queues
# import multiprocessing
# from multiprocessing import Array
#
# def foo(i, arg):
#     arg[i] = i + 100
#     for item in arg:
#         print(item)
#     print("==============")
#
#
# if __name__ == '__main__':
#     li = Array('i', 10)
#     for i in range(10):
#         p = Process(target=foo, args=(i, li, ))
#         p.start()



# from multiprocessing import Process
# from multiprocessing import queues
# import multiprocessing
# from multiprocessing import Manager
#
# def foo(i, arg):
#     arg[i] = i + 100
#     print(arg.values())
#
# if __name__ == '__main__':
#     obj = Manager()
#     li = obj.dict()
#     for i in range(10):
#         p = Process(target=foo, args=(i, li, ))
#         p.start()
#         p.join()
#     # import time
#     # time.sleep(0.1)
