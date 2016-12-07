#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# 写模块,模块名不要和python提供的内部模块重名,不然内部模块无法使用,

# import login
# import test.sa
#
# login.login()
# login.logout()
# test.sa.test()

import sys


# 单模块,在同一级目录下的: import <模块名>
# 嵌套在文件夹下的: from lib import sa
# 嵌套在多级文件夹下的(lib目录下,test目录下): from lib.test import sa
# 不同文件夹,重名模块: from lib import com as lib_com
#                    from  src import com as src_com


# import sys
# print(sys.path)
#
# 结果:
# ['/Users/lianliang/PycharmProjects/python_-study/day5', '/Users/lianliang/PycharmProjects/python_-study', '/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python35.zip', '/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5', '/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin', '/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/site-packages']

# import sys
# import time
#
#
# def view_bar(num, total):
#     rate = float(num) / float(total)
#     rate_num = int(rate * 100)
#     r = '\r%d%%' % (rate_num, )
#     sys.stdout.write(r)
#     sys.stdout.flush()
#
#
# if __name__ == '__main__':
#     for i in range(0, 101):
#         time.sleep(0.1)
#         view_bar(i, 100)

# import os

# print(os.getcwd())                 # 获取当前工作目录，即当前python脚本工作的目录路径
# print(os.chdir("/Users/lianliang"))         # 改变当前脚本工作目录；相当于shell下cd
# print(os.path.abspath(os.curdir))                   # 返回当前目录: ('.')
# print(os.path.abspath(os.pardir))                   # 获取当前目录的父目录字符串名：('..')
# os.makedirs('dir1/dir2')    # 可生成多层递归目录
# os.removedirs('dirname1')   # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')         # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')         # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')       # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()                 # 删除一个文件
# os.rename("oldname","new")  # 重命名文件/目录
# os.stat('/Users/lianliang/faceid-newground.tar.gz')   # 获取文件/目录信息
# print(os.sep)                      # 操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep                  # 当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# print(os.pathsep)                  # 用于分割文件路径的字符串
# print(os.name)                     # 字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")   # 运行shell命令，直接显示
# print(os.environ)                  # 获取系统环境变量
# os.path.abspath(path)       # 返回path规范化的绝对路径
# os.path.split(path)         # 将path分割成目录和文件名二元组返回
# os.path.dirname(path)       # 返回path的目录。其实就是os.path.split(path)的第一个元素
# os.path.basename(path)      # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)        # 如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)         # 如果path是绝对路径，返回True
# os.path.isfile(path)        # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)         # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)      # 返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)      # 返回path所指向的文件或者目录的最后修改时间

# import hashlib
#
# # ######## md5 ########
# hash = hashlib.md5()
# # help(hash.update)
# hash.update('admin')
# print(hash.hexdigest())
# print(hash.digest())
#
#
# ######## sha1 ########
#
# hash = hashlib.sha1()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())
#
# # ######## sha256 ########
#
# hash = hashlib.sha256()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())
#
#
# # ######## sha384 ########
#
# hash = hashlib.sha384()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())
#
# # ######## sha512 ########
#
# hash = hashlib.sha512()
# hash.update(bytes('admin', encoding='utf-8'))
# print(hash.hexdigest())


# import hmac
# import hashlib
#
# h = hmac.new(bytes('898oaFs09f',encoding="utf-8"))
# h.update(bytes('admin',encoding="utf-8"))
# print(h.hexdigest())
#
#
# hash = hashlib.md5(bytes('898oaFs09f',encoding="utf-8"))
# hash.update(bytes('admin',encoding="utf-8"))
# print(hash.hexdigest())


import random

print(random.random())
print(random.randint(1, 2))
print(random.randrange(1, 10))