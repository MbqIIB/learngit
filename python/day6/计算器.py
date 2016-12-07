#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import re

# number = input("请输入要计算的表达式")

input_num = input("请输入要计算的表达式:")

# r = re.search("\(([\+\-\*\/]*\d+\.*\d*){2,}\)", input_num).group()
# print(r)

# r = re.search("\((.*)\)", input_num).group(1)
# print(r)


# r = re.match("\(.*\)", number)
# print(r)
#
#
number = input_num
flag = True
while flag:
    if re.match("\(.*\)", number):
        num_expression = re.search("\(([\+\-\*\/]*\d+\.*\d*){2,}\)", number).group()
        num = re.search("\((\d+[\+\-\*\/]\d+)\)", num_expression).group(1)
        if re.match("\d+\+\d+", num):
            num_list = num.split('+')
            result = int(num_list[0]) + int(num_list[1])
            number = number.replace(num_expression, str(result))
        elif re.match("\d+\-\d+", num):
            num_list = num.split('-')
            result = int(num_list[0]) + int(num_list[1])
            number = re.sub(num_expression, str(result), number)
        elif re.match("\d+\*\d+", num):
            num_list = num.split('*')
            result = int(num_list[0]) + int(num_list[1])
            number = number.replace(num_expression, str(result))
        elif re.match("\d+\/\d+", num):
            num_list = num.split('/')
            result = int(num_list[0]) + int(num_list[1])
            number = number.replace(num_expression, str(result))
    elif re.match("\d+\+\d+", number):
        num_expression = re.search("\d+\+\d+", number).group()
        num = re.search("\d+\+\d+", number).group(1)
        num_list = num.split('+')
        result = int(num_list[0]) + int(num_list[1])
        number = number.replace(num_expression, str(result))
    elif re.match("\d+\-\d+", number):
        num_expression = re.search("\d+\-\d+", number).group()
        num = re.search("\d+\-\d+", number).group(1)
        num_list = num.split('-')
        result = int(num_list[0]) + int(num_list[1])
        number = number.replace(num_expression, str(result))
    elif re.match("\d+\*\d+", number):
        num_expression = re.search("\d+\*\d+", number).group()
        num = re.search("\d+\*\d+", number).group(1)
        num_list = num.split('*')
        result = int(num_list[0]) + int(num_list[1])
        number = number.replace(num_expression, str(result))
    elif re.match("\d+\/\d+", number):
        num_expression = re.search("\d+\/\d+", number).group()
        num = re.search("\d+\/\d+", number).group(1)
        num_list = num.split('/')
        result = int(num_list[0]) + int(num_list[1])
        number = number.replace(num_expression, str(result))
    elif re.match("[\+\-\*\/]]", number):
        flag = False
        print(number)






    # obj = re.findall('\d+', 'fa123uu888asf')
# print(obj)



# 替换
# content = "123abc456"
# # new_content = re.sub('\d+', 'sb', content)
# new_content = re.sub('\d+', 'sb', content, 1)
# print(new_content)

# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('\*', content)
# # new_content = re.split('\*', content, 1)
# print(new_content)


# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('[\+\-\*\/]+', content)
# # new_content = re.split('\*', content, 1)
# print(new_content)

# origin = "hasaabc dfuojqw halaabc m098u2934l"
# r = re.match("h\w+", origin).group()
# r = re.search("h(\w+)(\w+)", origin).groups()
# r = re.findall("h(\w+)a(ab)c", origin)
# print(r)
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果
# print(r.groupdict()) # 获取模型中匹配到的分组结果

 # 无分组
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("a(le)x", origin, 1)
# print(r)

# 有分组
#
# origin = "hello alex bcd alex lge alex acd 19"
# r1 = re.split("(alex)", origin, 1)
# print(r1)
# r2 = re.split("(())", number, 1)
# print(r2)






