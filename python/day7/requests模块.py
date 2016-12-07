#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# import urllib.request
#
#
# f = urllib.request.urlopen('http://www.example.com/')
# result = f.read().decode('utf-8')
# print(result)


# import urllib.request
#
# req = urllib.request.Request('http://www.example.com/')
# req.add_header('Referer', 'http://www.python.org/')
# f = urllib.request.urlopen(req)
#
# result = f.read().decode('utf-8')
# print(result)



# # 1、无参数实例
#
# import requests
#
# ret = requests.get('https://github.com/timeline.json')
#
# print(ret.url)
# print(ret.text)
#
#
#
# # 2、有参数实例
#
# import requests
#
# payload = {'key1': 'value1', 'key2': 'value2'}
# ret = requests.get("http://httpbin.org/get", params=payload)
#
# print(ret.url)
# print(ret.text)




# # 1、基本POST实例
#
# import requests
#
# payload = {"key1": "value1", "key2": "value2"}
# ret = requests.post("http://httpbin.org/post", data=payload)
#
# print(ret.text)
#
#
# # 2、发送请求头和数据实例
#
# import requests
# import json
#
# url = 'https://api.github.com/some/endpoint'
# payload = {"some": "data"}
# headers = {"content-type": "application/json"}
#
# ret = requests.post(url, data=json.dumps(payload), headers=headers)
#
# print(ret.text)
# print(ret.cookies)



# import urllib
# import requests
# from xml.etree import ElementTree as ET
#
# # 使用内置模块urllib发送HTTP请求，获得XML格式内容
#
# # r = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
# # result = r.read().decode('utf-8')
#
#
#
# # 使用第三方模块requests发送HTTP请求，获得XML格式内容
# r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=840787395')
# result = r.text
#
#
# # 解析XML格式内容
# node = ET.XML(result)
#
# print(node.text)
#
# # 获取内容
# if node.text == "Y":
#     print("在线")
# else:
#     print("离线")




import urllib
import requests
from xml.etree import ElementTree as ET

# 使用内置模块urllib发送HTTP请求，或者XML格式内容
"""
f = urllib.request.urlopen('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
result = f.read().decode('utf-8')
"""

# 使用第三方模块requests发送HTTP请求，或者XML格式内容
r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=G666&UserID=')
result = r.text

# 解析XML格式内容
root = ET.XML(result)
for node in root.iter('TrainDetailInfo'):
    print(node.find('TrainStation').text, node.find('StartTime').text, node.tag, node.attrib)