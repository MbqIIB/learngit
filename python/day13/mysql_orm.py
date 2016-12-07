#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
engine = create_engine("mysql+pymysql模块://root:@127.0.0.1:3306/test", max_overflow=5)

Base = declarative_base()


# 单表
# class Test(Base):
#     __tablename__ = 'test'
#     nid = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(32))


# 一对多
class Group(Base):
    __tablename__ = 'group'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(32))


class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    group_id = Column(Integer, ForeignKey('group.nid'))
    group = relationship("Group", backref='uuu')

    def __repr__(self):
        temp = "%s - %s: %s" %(self.nid, self.username, self.group_id)
        return temp


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)

init_db()
Session = sessionmaker(bind=engine)
session = Session()
#
# session.add(Group(caption='dba'))
# session.add(Group(caption='ddd'))
# session.commit()
#
# session.add_all([
#     User(username='alex1',group_id=1),
#     User(username='alex2',group_id=2)
# ])
# session.commit()

# # 只是获取用户
# ret = session.query(User).filter(User.username == 'alex1').all()
# print(ret)
# ret = session.query(User).all()
# obj = ret[0]
# print(ret)
# print(obj)
# print(obj.nid)
# print(obj.username)
# print(obj.group_id)
#
# ret = session.query(User.username).all()
# print(ret)
# sql = session.query(User,Group).join(Group, isouter=True)
# print(sql)
# ret = session.query(User,Group).join(Group, isouter=True).all()
# print(ret)
# select * from user left join group on user.group_id = group.nid


# 新方式(正向查询)
ret = session.query(User).all()
for obj in ret:
    # obj 代指user表的每一行数据
    # obj.group 代指group对象,
    print(obj.nid,obj.username, obj.group_id, obj.group, obj.group.nid, obj.group.caption)


