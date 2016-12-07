#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5
from 发布与订阅类 import RedisHelper

obj = RedisHelper()
obj.publish('test msg', 'fm111.7')