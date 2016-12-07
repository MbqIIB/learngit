#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian
import sys
import readline
import rlcompleter

if sys.platform == 'darwin' and sys.version_info[0] == 2:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")  # linux and python3 on mac for mac


'''
上面自己写的tab.py模块只能在当前目录下导入，
如果想在系统的何何一个地方都使用怎么办呢？
此时你就要把这个tab.py放到python全局环境变量目录里啦，
基本一般都放在一个叫 Python/2.7/site-packages 目录下，
这个目录在不同的OS里放的位置不一样，
用 print(sys.path) 可以查看python环境变量列表。
'''