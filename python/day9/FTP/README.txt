==================================================

                 FTP 服务

               * 多用户登录验证
               * 文件上传下载
               * 简单文件系统操作命令

==================================================
>>> Language : Python 3.5.1
>>> Date     :
>>> Coding   : coding:UTF-8
>>> author   : LiangXianSen
>>> E-mail   : lianglian8866@163.com
>>> blog知识点: http://www.cnblogs.com/liangxiansen/articles/5654749.html
>>> github   : https://github.com/LiangXianSen/python_-study/tree/master/day9





一.程序目录结构:

FTP
|   README.txt                      # 帮助文件
|
├── FTP_Client                      # ftp客户端
│   ├── __init__.py
│   ├── bin
│   │   └── client.py               # 客户端运行程序
│   ├── db
│   ├── etc
│   ├── lib                         # 程序公共代码库
│   │   └── utils.py                # 工具模块
│   └── src
│       └── socket_client.py        # 客户端源代码

└── FTP_Server                      # ftp服务端
    ├── __init__.py
    ├── bin
    │   ├── admin.py                # 用户管理程序
    │   └── server.py               # ftp服务端启动程序
    ├── db
    │   ├── data                    # 用户数据
    │   │   └── admin               # 用户家目录
    │   │       └── megvii_kas.auth # 用户上传得文件
    │   └── user.json               # 用户数据库
    ├── etc
    │   └── config.ini              # 服务器配置文件
    ├── lib
    │   └── utils.py                # 工具模块
    └── src
        ├── socket_server.py        # 服务端源代码
        └── user.py                 # 用户管理程序源代码



二.数据结构:
    位于服务端的db目录下user.json文件保存了ftp用户的账户信息,json格式的文件
    文件内容是字典格式:
        {用户名: {密码: '', 磁盘配额: 99999, .....}}



三.测试:
    用户:admin    密码:admin

    测试文件: megvii_kas.auth



四.启动说明:
    server端:    修改etc目录下config.ini配置文件,bin目录下运行: python server.py
                 用户管理程序,bin目录下运行: python admin.py


    client端:    bin目录下运行: python client.py {host} {prot}



五.使用命令:
socket 实现ftp
    实现功能:
        ls              查看文件
        cd              切换目录
        du              统计大小
        pwd             获取当前所在路径
        put             上传文件
        get             下载文件
        mkdir           创建目录
        remove          删除

    断点续传:            上传下载文件过程中程序意外中断或退出,下次再操作时可以继续之前的进度.

    进度条:              上传下载文件时实时显示进度.


