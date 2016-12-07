#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5
from 发布与订阅类 import RedisHelper

obj = RedisHelper()
data = obj.subscribe('fm111.7')
print(data.parse_response())