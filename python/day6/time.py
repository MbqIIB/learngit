#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import time
import datetime

print(time.clock()) #返回处理器时间,3.3开始已废弃
print(time.process_time()) #返回处理器时间,3.3开始已废弃
print(time.time()) #返回当前系统时间戳
print(time.ctime()) #输出Tue Jan 26 18:23:48 2016 ,当前系统时间
print(time.ctime(time.time()-86400)) #将时间戳转为字符串格式
print(time.gmtime(time.time()-86400)) #将时间戳转换成struct_time格式
print(time.localtime(time.time()-86400)) #将时间戳转换成struct_time格式,但返回 的本地时间
print(time.mktime(time.localtime())) #与time.localtime()功能相反,将struct_time格式转回成时间戳格式
time.sleep(4) #sleep,等待4秒
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将struct_time格式转成指定的字符串格式
print(time.strptime("2016-01-28","%Y-%m-%d") ) #将字符串格式转换成struct_time格式

#datetime module

print(datetime.date.today()) #输出格式 2016-01-26
print(datetime.date.fromtimestamp(time.time()-86400) ) #2016-01-16 将时间戳转成日期格式
current_time = datetime.datetime.now() #
print(current_time) #输出2016-01-26 19:04:30.335935
print(current_time.timetuple()) #返回struct_time格式
datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
print(current_time.replace(2014,9,12)) #输出2014-09-12 19:06:24.074900,返回当前时间,但指定的值将被替换

str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") #将字符串转换成日期格式
print(str_to_date)

new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
new_date = datetime.datetime.now() + datetime.timedelta(days=-10) #比现在减10天
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10) #比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) #比现在+120s
print(new_date)