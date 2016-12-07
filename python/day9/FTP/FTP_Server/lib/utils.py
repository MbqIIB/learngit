#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import sys
import time
import hashlib
import configparser


def md5(arg):
    """
    md5加密
    :param arg:
    :return:
    """
    # 额外key加密
    obj = hashlib.md5(bytes('woyaojueqi', encoding='utf-8'))
    obj.update(bytes(arg, encoding='utf-8'))
    return obj.hexdigest()


class Config:
    """
    读取配置文件
    """
    def __init__(self, config_path, section='DEFAULTS'):
        self.section = section
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(config_path, encoding='utf-8')

    def __getattr__(self, item):
        return self.config.get(self.section, item)


class ProgressBar:
    """
    进度条
    """
    def __init__(self, width=50):
        self.width = width

    def update(self, number, total):
        """
        刷新进度
        :param number: 当前值
        :param total:  总数
        :return:
        """
        remainder, quotient = divmod(number*100, total)  # 求商和余数
        assert 0 <= remainder <= 100  # `x`: progress in percent ( between 0 and 100)
        pointer = int(self.width * (remainder / 100.0))  # 取整
        sys.stdout.write('\r%d%% [%s]' % (int(remainder), '#' * pointer + '.' * (self.width - pointer)))
        sys.stdout.flush()
        time.sleep(0.1)
