#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# from sqlalchemy import create_engine
# # 建立连接,必须按照这个格式
# engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test", max_overflow=5, )
#
# # 执行SQL
# cur = engine.execute("update host set ip = '7.7.7.77' where hostname = 'c7'")
#
# # 执行SQL
# cur = engine.execute("insert into host(hostname,port,ip)value(%s,%s,%s)", [("c6", 22, "6.6.6.6"), ("c7", 22, "7.7.7.7")])
# # 获取最新自增ID
# print(cur.lastrowid)
#
#
# # 执行SQL
# # cur = engine.execute("select * from host")
# # 获取第一行数据
# cur.fetchone()
# # 获取第n行数据
# cur.fetchmany(3)
# # 获取所有数据
# cur.fetchall()


# from sqlalchemy import create_engine
#
#
# engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/s11", max_overflow=5)
#
#
# # 事务操作
# with engine.begin() as conn:
#     conn.execute("insert into table (x, y, z) values (1, 2, 3)")
#     conn.execute("my_special_procedure(5)")
#
#
# conn = engine.connect()
# # 事务操作
# with conn.begin():
#        conn.execute("some statement", {'x': 5, 'y': 10})


from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
# import pymysql
engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test", max_overflow=5, )
'''
    max_overflow是最大连接数
    其他方法：
    “charset”指定了连接时使用的字符集（可省略）=utf8
    echo 参数为 True 时，会显示每条执行的 SQL 语句，生产环境下关闭。
'''
# 连接数据库
conn = engine.connect()
# 获取数据库表元数据,创建表必须
metadata = MetaData()
# 定义表
user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )

color = Table('color', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    )

# 创建数据表，如果数据表存在，则忽视
metadata.create_all(engine)

# user表创建SQL语句，INSERT INTO "user" (id, name) VALUES (:id, :name)
sql = user.insert().values(id=666, name='liang')
conn.execute(sql)

# 删除一条user表里的 条件是id大于1的
sql = user.delete().where(user.c.id > 1)
conn.execute(sql)

# 更新
sql = user.update().where(user.c.name == 'liang').values(name='lianglian')
conn.execute(sql)

from sqlalchemy import select  # 其他模块相同
sql = select([user, ])
res =conn.execute(sql)
print(res.fetchall())


# 也可以直接写SQL执行
cur = engine.execute("update user set name = 'lianglian' where name = 'liang'")

# 执行SQL
cur = engine.execute("insert into user(id,name)value(%s,%s)", [(2, "aaa"), (3, "bbb")])
# 获取最新自增ID
print(cur.lastrowid)
# 执行SQL
cur = engine.execute("select * from user")
# 获取第一行数据
cur.fetchone()
# 获取第n行数据
cur.fetchmany(3)
# 获取所有数据
cur.fetchall()
conn.close()



