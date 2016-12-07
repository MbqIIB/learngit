#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

"""
网银购物配置文件

"""
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

ATM_LOG_PATH=os.path.join(BASE_DIR, 'log', 'ATM', 'ATM_server.log')
SHOP_PRODUCT_DIR = os.path.join(BASE_DIR, 'db', 'product')
DATA_DIR = os.path.join(BASE_DIR, 'db', 'data')

ATM_LOG_LEVEL="INFO"
SHOP_LEVEL="DEBUG"

