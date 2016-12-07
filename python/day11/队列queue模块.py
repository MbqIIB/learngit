#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import queue
# 先进先出队列
# put放数据,是否阻塞,阻塞时的超时时间
# get取数据(默认堵塞),是否阻塞,阻塞时的超时时间

# 队列最大长度,
# qsize()真实队列个数
# maxsize 最大支持的个数
# join,阻塞进程,当队列中任务执行完毕后(task_done),不再阻塞


# q = queue.Queue(2)  # 队列最大长度
# print(q.empty())    # 检查是否为空(初始默认是空)
# q.put(11)
# q.put(22)
# print(q.empty())
# print(q.qsize())   # 获取队列长度
# # q.put(22)
# q.put(33, block=False)  # 不堵塞
# q.put(33, block=False, timeout=2)  # 不堵塞,等待2秒
# print(q.get())
# print(q.get())

# print(q.get(timeout=2))


# import queue               #先进先出
# q = queue.LifoQueue()
# q.put(123)
# q.put(456)
# print(q.get())


# q = queue.PriorityQueue()   # 根据优先级处理,数字最小的优先级最高
# # put() 参数一为优先级,第二个参数是value
# q.put((3, "alex3"))
# q.put((2, "alex2"))
# q.put((1, "alex1"))
# print(q.get())

q= queue.deque()          #双向队列
q.append((123))
q.append(234)
q.appendleft(456)
print(list(q))
q.pop()
q.popleft()
print(list(q))



