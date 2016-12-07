#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# best_img = []
# idcard_img = []
#
# dic = {}
# with open('/Users/lianliang/Desktop/face/GROUP2/test', 'r') as file:
#     for line in file:
#         best, idcard = line.split(',')[0:2]
#         if best not in best_img:
#             best_img.append(best)
#         elif idcard not in idcard_img:
#             idcard_img.append(idcard)
#
# with open('/Users/lianliang/Desktop/face/GROUP2/test', 'r') as file:
#     for line in file:
#         for img in best_img:
#             dic[img] = 0
#             if img in line:
#                 dic[img] += 1
#
#
# print(dic)


# for img in best_img:
#     num = 0
#     with open('/Users/lianliang/Desktop/face/GROUP2/test', 'r') as file:
#         for line in file:
#             if img in line:
#                 num += 1
#             if num >= 1600:
#                 print(img)



# rows=6
# i=5
# for f in range(rows):
#     msg = " "
#     num = i
#     for a in range(f):
#         msg += " " * a
#         num-=1
#
#     for b in range(0, 2*f-1):
#         msg += "*"
#         b+=1
#
#     # i+=1
#     print msg


# rows=6   # 指定金字塔高度
# for i in range(rows):   # 循环
#     msg = ''    # 定义空字符串
#     msg += ' ' * (rows-i-1)    # 一行中空白部分
#     msg += '*' * (2*i+1)       # 一行中金字塔部分
#     print msg   # 打赢字符串拼接得内容

rows = 6
for i in range(rows):
    print ' ' * (rows - i - 1) + '*' * (2 * i + 1)




















# rows=6
# i=5
# for i in range(0,rows):
#     for a in range(i,0):
#         print" "
#         a-=1
#     for b in range(0,2*i-1):
#         print"*",
#         b+=1
#     i+=1
#     print"\n"




