#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# from configparser import ConfigParser
#
# etc = ConfigParser(allow_no_value=True)
#
# etc.read("./conf/conf.py")
#
# sectiions = etc.sections()
# print(sectiions)
#
# options = etc.options(sectiions[1])
# print(options)
#
# items = etc.items(section='log', )
# print(items)
#
# import os
#
# config_ini = os.path.abspath("./conf/conf.py",)
#
# def config_read(sectiions, options, file_ini=config_ini):
#     import os
#     from configparser import ConfigParser
#     if os.path.exists(file_ini):
#         etc = ConfigParser()
#         etc.read(file_ini, encoding='utf-8')
#         return etc.items(sectiions, options, )





# class Config(object):
#     def __init__(self, config_path, section='DEFAULTS'):
#         self.section = section
#         self.etc = ConfigParser(allow_no_value=True)
#         self.etc.read(config_path)
#
#     def __getattr__(self, item):
#         return self.etc.get(self.section, item)


