#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


import shutil
#
# shutil.copyfileobj(open('old.xml', 'r', encoding='utf-8'), open('new.xml', 'w', encoding='utf-8'))

# shutil.copy2('old.xml', 'new.xml')


# import shutil
# # 拷贝文件夹,排除*.pyc,tmp*的文件
# shutil.copytree('/Users/lianliang/PycharmProjects/python_-study/day5', '/Users/lianliang/test', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))


# import shutil
# # 拷贝文件夹,排除*.pyc,tmp*的文件
# shutil.copytree('/Users/lianliang/PycharmProjects/python_-study/day5', '/Users/lianliang/test', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))



# import shutil
#
# shutil.rmtree('/Users/lianliang/test')


# import shutil
#
# shutil.move('/Users/lianliang/test', '/Users/lianliang/aaa/')



# #将 /Users/lianliang/aaa/ 下的文件打包放置当前程序目录
# import shutil
# ret = shutil.make_archive("wwwwwwwwww", 'gztar', root_dir='/Users/lianliang/aaa')
# print(ret)
#
# #将 /Users/lianliang/ 下的文件打包放置 /Users/lianliang/目录
# import shutil
# ret = shutil.make_archive("/Users/lianliang/wwwwwwwwww", 'gztar', root_dir='/Users/lianliang/aaa')
# print(ret)




# import zipfile
#
# # 压缩
# z = zipfile.ZipFile('test.zip', 'w')
# z.write('txt')
# z.write('XML.py')
# z.close()
#
# # 解压
# z = zipfile.ZipFile('test.zip', 'r')
# ret = z.namelist()
# print(ret)
#
# z.extract('txt')




# import tarfile
#
# # 压缩
# tar = tarfile.open('test.tar.gz', 'w')
# tar.add('./txt', arcname='txt文件')
# tar.add('./new.xml', arcname='new')
# tar.close()
#
# # 解压
# tar = tarfile.open('test.tar.gz', 'r')
# ret = tar.getnames()
# tar.extract('new')


