#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# import os
#
# FILE_DIR = "/Users/lianliang"
#
# file_list = os.listdir(FILE_DIR)
# for file in file_list:
#     file_path = os.path.join(FILE_DIR, file)
#     print(file_path)

import re



# # 无分组
# origin = "hasaabc dfuojqw halaabc m098u2934l"
# r = re.search("ha\w+", origin)
# print(r.group())  # 获取匹配到的所有结果
# print(r.groups())  # 获取模型中匹配到的分组结果
# print(r.groupdict())  # 获取模型中匹配到的分组结果
#
# # 有分组
# r = re.search("(ha)(\w+)", origin)
# print(r.group())  # 获取匹配到的所有结果
# print(r.groups())  # 获取模型中匹配到的分组结果
# print(r.groupdict())  # 获取模型中匹配到的分组结果



# # 无分组
# origin = "hasaabc dfuojqw halaabc m098u2934l"
# r = re.findall("ha\w+", origin)
# print(r)  # 获取匹配到的所有结果
#
# # 有分组
# r = re.findall("(ha)(\w+)", origin)
# print(r)  # 获取匹配到的所有结果
#
#
# # 无分组
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("alex", origin, 1)
# print(r)
#
# # 有分组
#
# origin = "hello alex bcd alex lge alex acd 19"
# r1 = re.split("(alex)", origin, 1)
# print(r1)
# r2 = re.split("(al(ex))", origin, 1)
# print(r2)


