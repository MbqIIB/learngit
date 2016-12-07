#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import os
import sys

# 将程序目录添加到sys.path里面
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.mall import shopping as shop

if __name__ == '__main__':
    shop.run()