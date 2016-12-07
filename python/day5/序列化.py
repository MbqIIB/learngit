#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import json
dic = {'k1': 'v1'}
print(dic, type(dic))

# 将python基本数据类型转化成字符串形式
result = json.dumps(dic)
print(result, type(result))


s1 = '{"k1": "123"}'   # 通过json.loads反序列化,字符串一定要使用双引号("),因为在其语言中单引号是字符,双引号是字符串

# 将字符串形式转换成python的基本数据类型
dic = json.loads(s1)
print(dic, type(dic))


json.dump(dic, open('test.json', 'w'))   # 写入文件
res = json.load(open('test.json', 'r'))  # 从文件读出
print(res)




import pickle

li = [11, 22, 33]
r = pickle.dumps(li)
print(r)

result = pickle.loads(r)
print(result)


li = [11, 22, 33]
pickle.dump(li, open('db', 'wb'))  # 写到文件

result = pickle.load(open('db', 'rb'))  # 从文件中载入
print(result)


# pickle/json
#
# json更加适合跨语言,字符串基本数字类型序列话
# pickle仅适用于python,python所有类型的序列化,




# import requests
# import json
#
# response = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
# response.encoding = 'utf-8'
#
# dic = json.loads(response.text)
# print(dic)


import time

# # 返回当前系统时间戳
# print(time.time())
#
# # 输出当前系统时间,字符串格式
# print(time.ctime())


# print(time.ctime(time.time()-86400))

