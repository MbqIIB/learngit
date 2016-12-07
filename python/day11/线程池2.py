#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import queue
import threading
import contextlib
import time

StopEvent = object()


class ThreadPool(object):

    def __init__(self, max_num):
        # 创建任务队列
        self.q = queue.Queue()
        # 获取最大数设置
        self.max_num = max_num

        self.terminal = False
        # 创建任务线程的list
        self.generate_list = []
        # 创建存放空闲进程的list
        self.free_list = []

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数，回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        # 空闲的线程等于0,并且已经生成的线程小于线程最大设置就生成一个线程
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            # 创建线程
            self.generate_thread()
        # 获取的任务
        w = (func, args, callback,)
        # 放进队列里面
        self.q.put(w)

    def generate_thread(self):
        """
        创建一个线程
        """
        # 创建一个线程去队列中取一个任务执行
        t = threading.Thread(target=self.call)
        # 运行线程
        t.start()

    def call(self):
        """
        循环去获取任务函数并执行任务函数
        """
        # 创建线程
        current_thread = threading.currentThread
        # 将线程加到任务线程列表中
        self.generate_list.append(current_thread)
        # 从队列中获取任务
        event = self.q.get()
        while event != StopEvent:
            # 得到任务元祖(函数,参数,函数名)
            func, arguments, callback = event
            try:
                # 执行函数得到返回值结果
                result = func(*arguments)
                success = True
            except Exception as e:
                success = False
                result = None
            # 如果有第二个函数
            if callback is not None:
                try:
                    # 执行第二个函数
                    callback(success, result)
                except Exception as e:
                    pass
            # 线程执行完任务放到调用任务状态转换得方法,将执行完的线程放到空闲的list中
            with self.worker_state(self.free_list, current_thread):
                # 判断是否终止
                if self.terminal:
                    # 终止循环
                    event = StopEvent
                else:
                    # 有则继续取任务,执行任务
                    event = self.q.get()
        else:
            # 线程执行完从已经创建得线程列表中删除
            self.generate_list.remove(current_thread)

    def close(self):
        """
        执行完所有的任务后，所有线程停止
        """
        full_size = len(self.generate_list)
        while full_size:
            self.q.put(StopEvent)
            full_size -= 1

    def terminate(self):
        """
        无论是否还有任务，终止线程
        """
        self.terminal = True

        while self.generate_list:
            self.q.put(StopEvent)

        self.q.empty()


    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
        """
        用于记录线程中正在等待的线程数
        """
        state_list.append(worker_thread)
        try:
            yield
        finally:
            state_list.remove(worker_thread)


"""
# How to use


pool = ThreadPool(5)

def callback(status, result):
    # status, execute action status
    # result, execute action return value
    pass


def action(i):
    time.sleep(1)
    print(i)

for i in range(30):
    ret = pool.run(action, (i,), callback)

# pool.close()
# pool.terminate()
"""