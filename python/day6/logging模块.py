#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# import logging
#
#
# logging.basicConfig(filename='log.log',
#                     format='%(asctime)s - %(name)s - %(levelname)s :  %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S %p',
#                     level=10)
#
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# logging.log(10, 'log')



# import logging
#
# # 定义文件
# file_1_1 = logging.FileHandler('l1_1.log', 'a', encoding='utf-8')
# fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s")
# file_1_1.setFormatter(fmt)
#
# file_1_2 = logging.FileHandler('l1_2.log', 'a', encoding='utf-8')
# fmt = logging.Formatter()
# file_1_2.setFormatter(fmt)
#
# # 定义日志
# logger1 = logging.Logger('s1', level=logging.ERROR)
# logger1.addHandler(file_1_1)
# logger1.addHandler(file_1_2)
#
#
# # 写日志
# logger1.critical('1111')


# import logging
#
# # 定义文件
# file_2_1 = logging.FileHandler('l2_1.log', 'a')
# fmt = logging.Formatter()
# file_2_1.setFormatter(fmt)
#
# # 定义日志
# logger2 = logging.Logger('s2', level=logging.INFO)
# logger2.addHandler(file_2_1)
#
# # 写日志
# logger2.critical('l2-test')