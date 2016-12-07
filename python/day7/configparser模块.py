#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# import configparser
#
# etc = configparser.ConfigParser()
# etc.read('./etc.ini', encoding='utf-8')
# sections = etc.sections()
# print(sections)
# key_value = etc.items('section1')
# print(key_value)
# options = etc.options('section1')
# print(options)
#


import configparser

config = configparser.ConfigParser()
config.read('etc.ini', encoding='utf-8')


# 检查
option = config.has_option('section1', 'k1')
print(option)

# 删除节点
config.remove_option("section1", 'k1')
config.write(open('etc.ini', 'w'))

# 设置
config.set("section1", 'k10', '10000')
config.write(open('etc.ini', 'w'))

