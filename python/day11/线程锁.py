#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# 未加锁
# import threading
# import time
#
# NUM = 10
#
# def func(arg):
#     global NUM
#     NUM -= 1
#     time.sleep(1)
#     print(NUM)
#
# for i in range(10):
#     t = threading.Thread(target=func, args=(i, ))
#     t.start()



# import threading
# import time
#
# NUM = 10
#
# def func(lock):
#     global NUM
#     #上锁
#     lock.acquire()
#     NUM -= 1
#     time.sleep(2)
#     print(NUM)
#     # 开锁
#     lock.release()
#
# lock = threading.Lock()  # 创建锁对象(只能锁一次)
# lock = threading.RLock()   # 创建锁对象(能迭代锁多次)
#
# for i in range(10):
#     t = threading.Thread(target=func, args=(lock, ))
#     t.start()



# import threading
# import time
#
# NUM = 10
#
# def func(lock):
#     global NUM
#     #上锁
#     lock.acquire()  # 锁1,锁住
#     NUM -= 1
#     lock.acquire()  # 锁2,锁住
#     time.sleep(2)
#     lock.release()  # 锁2,解锁
#     print(NUM)
#     # 开锁
#     lock.release()  # 锁1,解锁
#
# # lock = threading.Lock()  # 只能锁一次
# lock = threading.RLock()   # 能迭代锁多次
#
# for i in range(10):
#     t = threading.Thread(target=func, args=(lock, ))
#     t.start()



# import threading
# import time
#
# NUM = 10
#
# def func(i,lock):
#     global NUM
#     # 上锁5
#     lock.acquire()
#     NUM -= 1
#     time.sleep(1)
#     print(NUM, i)
#     # 开锁5
#     lock.release()
#
# lock = threading.BoundedSemaphore(5)   # 创建锁对象,(一次锁多个,释放多个)
#
# for i in range(10):
#     t = threading.Thread(target=func, args=(i, lock, ))
#     t.start()



# import threading
#
#
# def func(i, e):
#     print(i)
#     e.wait()   # 检测是什么灯,如果是红灯停;绿灯行
#     print(i+100)
#
#
# event = threading.Event()    # 创建锁对象
#
# for i in range(10):
#     t = threading.Thread(target=func, args=(i, event, ))
#     t.start()
#
# event.clear()  # 设置成红灯
# inp = input(">>>")
# if inp == "1":
#     event.set()  # 设置成绿灯




# # 输入多少放出多少
# import threading
# def func(i, con):
#     print(i)
#     con.acquire()
#     con.wait()    # 对应到notify的输入多少放出多少
#     print(i+100)
#     con.release()
#
#
# c = threading.Condition()
#
# for i in range(10):
#     t = threading.Thread(target=func, args=(i, c, ))
#     t.start()
#
#
# while True:
#     inp = input('>>>')
#     if inp == 'q':
#         break
#     c.acquire()
#     c.notify(int(inp))
#     c.release()



# 当某个执行结果为真就放出一个
import threading


def condition():
    ret = False
    r = input('>>>')
    if r == '1':
        ret = True
    else:
        ret = False
    return ret


def func(i, con):
    print(i)
    con.acquire()
    con.wait_for(condition)  # 检测condition函数执行结果,True放出一个
    print(i+100)
    con.release()

con = threading.Condition()

for i in range(10):
    t = threading.Thread(target=func, args=(i, con, ))
    t.start()


# import threading
#
# def condition_func():
#
#     ret = False
#     inp = input('>>>')
#     if inp == '1':
#         ret = True
#
#     return ret
#
#
# def run(n):
#     con.acquire()
#     con.wait_for(condition_func)
#     print("run the thread: %s" %n)
#     con.release()
#
# if __name__ == '__main__':
#
#     con = threading.Condition()
#     for i in range(10):
#         t = threading.Thread(target=run, args=(i,))
#         t.start()



# # 设置这个线程执行一次要多久
# from threading import Timer
#
#
# def hello():
#     print("hello, world")
#
# t = Timer(10, hello)  # hello任务执行设置执行10秒
# t.start()  # after 1 seconds, "hello, world" will be printed