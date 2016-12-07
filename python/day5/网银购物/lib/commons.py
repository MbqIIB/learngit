#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import hashlib

def md5(arg):
    obj = hashlib.md5(bytes('woyaojueqi', encoding='utf-8'))
    obj.update(bytes(arg, encoding='utf-8'))
    return obj.hexdigest()
