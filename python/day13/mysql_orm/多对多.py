#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
# 创建数据库引擎
engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test?charset=utf8", encoding="utf-8", echo=True)
# 生成一个SqlORM 基类
Base = declarative_base()

# 定义表结构,继承SqlORM基类
class HostToHostUser(Base):
    """关联表"""
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer, primary_key=True, autoincrement=True)

    # 外键,正向通过这个表这个字段可以找到host表中的nid对于
    host_id = Column(Integer, ForeignKey('host.nid'))
    # 外键,正向通过这个表这个字段可以找到host_user表中的nid对应
    host_user_id = Column(Integer, ForeignKey('host_user.nid'))

    # 关联,通过这个可以联系到host表
    host = relationship("Host", backref='h')
    # 关联,通过这个可以联系到host_user表
    host_user = relationship("HostUser", backref='u')


class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))


class Host(Base):
    __tablename__ = 'host'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))

    # 间接关联,中间通过一个
    host_user = relationship("HostUser", secondary=lambda: HostToHostUser.__table__, backref='h')


def init_db():
    """
    创建所有表
    :return:
    """
    Base.metadata.create_all(engine)


def drop_db():
    """
    删除所有表
    :return:
    """
    Base.metadata.drop_all(engine)

init_db()

# bind绑定
# 创建与数据库的会话session class
# 注意,这里返回给Session的是个class,不是实例
Session = sessionmaker(bind=engine)
session = Session()


# session.add_all([
#     Host(hostname='c1',port='22',ip='1.1.1.1'),
#     Host(hostname='c2',port='22',ip='1.1.1.2'),
#     Host(hostname='c3',port='22',ip='1.1.1.3'),
#     Host(hostname='c4',port='22',ip='1.1.1.4'),
#     Host(hostname='c5',port='22',ip='1.1.1.5'),
# ])
# session.commit()
#
#
# session.add_all([
#     HostUser(username='root'),
#     HostUser(username='db'),
#     HostUser(username='nb'),
#     HostUser(username='sb'),
# ])
# # 提交修改
# session.commit()
#
# session.add_all([
#     HostToHostUser(host_id=1,host_user_id=1),
#     HostToHostUser(host_id=1,host_user_id=2),
#     HostToHostUser(host_id=1,host_user_id=3),
#     HostToHostUser(host_id=2,host_user_id=2),
#     HostToHostUser(host_id=2,host_user_id=4),
#     HostToHostUser(host_id=2,host_user_id=3),
# ])
# session.commit()

# 获取主机1中所有用户
# 传统方法
# # 查询Host表中hostname等于'c1'的,等到匹配数据的Host类对象(因为那一行是用Host类创建的)
# host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
# # 查询HostToHostUser表结构中host_id == 1(host表中'c1'主机的nid)得到对应的host_user_id
# # SELECT host_to_host_user.host_user_id AS host_to_host_user_host_user_id FROM host_to_host_user
# host_2_host_user = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == host_obj.nid).all()
#
# r = zip(*host_2_host_user)  # 将得到的host_user_id数据去掉list中的元祖
# users = session.query(HostUser.username).filter(HostUser.nid.in_(list(r)[0])).all()
# print(users)


# 新方法
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
for item in host_obj.h:
    print(item.host_user.username)


host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
for item in host_obj.host_user:
    print(item.username)

