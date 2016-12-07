#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# for i in range(10):
#     if i == 3:
#         break
#     print(i)

# 输出0-9中得基数
# for i in range(10):
#     if i%2 == 0 :
#         continue
#     print(i)




# import time
# count = 0
# run_forever = True
# while run_forever:
#     count += 1
#     print("loop",count)
#     if count == 9:
#         run_forever = False   # 这样下面得语句还能执行,只有回到开头得时候发现调节不满足才会不执行;
#         #break                # 这个方法会直接跳出循环;
#     time.sleep(10)



# 跳出多重循环
# loop1 = 0   # 设定loop1 and loop2这两个计数器
# loop2 = 0
# while True:
#     loop1 += 1
#     print("loop1", loop1)
#     break_flag = False  # 在父循环中设定一个跳出标志,子循环只要想连父亲一块跳出时,就把这个标志改成True
#
#     while True:
#         loop2 += 1
#         if loop2 == 5:
#             break_flag = True
#             break
#         print('loop2', loop2)
#     if break_flag:
#         print("接到子循环跳出通知,我也得跳了!")
#         break


loop1 = 0   # 设定loop1 and loop2这两个计数器
loop2 = 0
flag = True
while flag:
    loop1 += 1
    print("loop1", loop1)

    while True:
        loop2 += 1
        if loop2 == 5:
            flag = False  # 循环到子级里面，想退出，我退出这级退出得同时还需要让父级也退出不循环了，设置得这个循环条件就起到作用了，设置为False
            break         #  跳出我自己这级循环
        print('loop2', loop2)