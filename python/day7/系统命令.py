#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

import subprocess
#
# ret = subprocess.call(["ls", "-l"], shell=False)  # 使用shell=False 就需要传一个拼接命令的序列
# ret = subprocess.call("ls -l", shell=True)   # 使用shell=True 传递完整的命令字符串
# print(ret)


# ret = subprocess.check_output(["echo", "Hello World!"])
# ret = subprocess.check_output("exit 1", shell=True)
# print(ret)


# import subprocess
# ret1 = subprocess.Popen(["df","-h"])
# ret2 = subprocess.Popen("df -h", shell=True)


# import subprocess
#
# obj = subprocess.Popen("touch aaa", shell=True, cwd='/Users/lianliang',)


# import subprocess
#
# obj = subprocess.Popen(["python3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# obj.stdin.write("print(1)\n")
# obj.stdin.write("print(2)")
# obj.stdin.close()
#
# cmd_out = obj.stdout.read()
# obj.stdout.close()
# cmd_error = obj.stderr.read()
# obj.stderr.close()
#
# print(cmd_out)
# print(cmd_error)


# import subprocess
#
# obj = subprocess.Popen(["python3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
# obj.stdin.write("print(1)\n")
# obj.stdin.write("print(2)")
#
# out_error_list = obj.communicate()  # 元祖的形式,返回stdout内容和stderr内容
# print(out_error_list)
# print(out_error_list[0])   # stdout
# print(out_error_list[1])   # stderr


import subprocess

obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
out_error_list = obj.communicate('print("hello")\nprint(123)')
print(out_error_list)



