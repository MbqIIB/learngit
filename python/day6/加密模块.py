#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian
import hashlib

obj = hashlib.md5(bytes('woyaojueqi', encoding='utf-8'))
obj.update(bytes('liang', encoding='utf-8'))
result = obj.hexdigest()
print(result)