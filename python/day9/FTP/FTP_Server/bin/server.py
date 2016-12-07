#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

import os
import sys
import socketserver

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.socket_server import MyServer
from lib.utils import Config

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'etc', 'config.ini')
CONFIG = Config(config_path, section='SERVER')


if __name__ == '__main__':
    run = socketserver.ThreadingTCPServer((CONFIG.listen, int(CONFIG.port)), MyServer)
    run.serve_forever()