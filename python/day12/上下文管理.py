#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# import contextlib
# @contextlib.contextmanager
# def worker_state(state_list, worker_thread):
#     print(999)
#     state_list.append(worker_thread)
#     try:
#         yield
#     finally:
#         state_list.remove(worker_thread)
#
#
# free_list = []
# current_thread = "alex"
# with worker_state(free_list, current_thread):
#     print(123)
#     print(456)



import contextlib
import socket

@contextlib.contextmanager
def context_socket(host, port):
    sk = socket.socket()
    sk.bind((host, port))
    sk.listen(5)
    try:
        yield sk
    finally:
        sk.close()


with context_socket('127.0.0.1', 8888) as sock:
    print(sock)
    print(socket)