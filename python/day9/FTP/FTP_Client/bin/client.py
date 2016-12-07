#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.socket_client import Client

if __name__ == '__main__':
    # host, port = (sys.argv[1], int(sys.argv[2]))
    host, port = ('127.0.0.1', 8888)  # IDE调试
    obj = Client(host, port)
    obj.mian()