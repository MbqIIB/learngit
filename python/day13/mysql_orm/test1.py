#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Liang Lian
# Python 3.5

# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy import create_engine
#
# # 生成一个SqlORM 基类
# Base = declarative_base()
# #
# engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test", echo=True)
#
# class Host(Base):
#     # 表名为hosts
#     __tablename__ = 'hosts'
#     # 表结构
#     # primary_key等于主键
#     # unique唯一
#     # nullable非空
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     hostname = Column(String(64), unique=True, nullable=False)
#     ip_addr = Column(String(128), unique=True, nullable=False)
#     port = Column(Integer, default=22)
#
# Base.metadata.create_all(engine)   # 创建所有表结构
#
# if __name__ == '__main__':
#     SessionCls = sessionmaker(bind=engine)
#     bind绑定
#     创建与数据库的会话session class
#     注意,这里返回给session的是个class,不是实例
#     session = SessionCls()
#     #插入字段
#     h1 = Host(hostname='redhat', ip_addr='1.1.1.1')
#     h2 = Host(hostname='ubuntu', ip_addr='2.2.2.2', port=80)
#     h3 = Host(hostname='mysql', ip_addr='3.3.3.3', port=3306)
#     # 添加一个字段
#     # session.add(h3)
#     # 添加多个字段
#     session.add_all([h1, h2, h3])
#     # 修改字段名字,只要没提交,此时修改也没问题
#     # h2.hostname = 'ubuntu_test'
#     # 支持数据回滚
#     # session.rollback()
#     # 提交
#     session.commit()


# ########### 增 ##########
# # 定义一个字段
# zenjia = Host(hostname='aaa', ip_addr='4.4.4.4')
# # 添加字段
# session.add(zenjia)
# # 添加多个字段
# session.add_all([
#     Host(hostname='bbb', ip_addr='5.5.5.5'),
#     Host(hostname='ccc', ip_addr='6.6.6.6')
# ])
# # 提交以上操作
# session.commit()


# ########## 删除 ##########
# # 过滤user表中id大于3的数据删除
# session.query(Host).filter(Host.id > 3).delete()
# session.commit()


# ########## 修改 ##########
# session.query(Host).filter(Host.hostname == 'ccc').update({"hostname": "c6"})
# session.query(Host).filter(Host.hostname == 'c6').update({Host.hostname: Host.hostname + "ccc"}, synchronize_session=False)
# session.query(Host).filter(Host.id > 3).update({Host.port: Host.port + 1}, synchronize_session="evaluate")
# session.commit()



######### 查询 ##########
# 查询Host表中hostname='aaa'的所有数据
# ret = session.query(Host).filter_by(hostname='aaa').all()
# print(ret)
# for i in ret:
#     print(i.hostname, i.ip_addr, i.port)
#
#
# # 查询Host表中hostname='aaa'的第一条数据
# ret = session.query(Host).filter_by(hostname='aaa').first()
# print(ret.hostname, ret.ip_addr, ret.port)
#
#
# # 查询Host表中ip_addr字段里面有等于1.1.1.1或者等于3.3.3.3的数据
# ret = session.query(Host).filter(Host.ip_addr.in_(['1.1.1.1', '3.3.3.3'])).all()
# for i in ret:
#     print(i.hostname, i.ip_addr, i.port)
#
#
# # 可以给返回结果起一个别名
# ret = session.query(Host.hostname.label('alias')).all()
# print(ret, type(ret))
#
# # 查询Host表,根据id排序
# ret = session.query(Host).order_by(Host.id)[0:3]
# for i in ret:
#     print(i.id, i.hostname, i.ip_addr, i.port,)
#
#
# # 创建query查询,filter是where条件,最后调用one()返回唯一行,如果调用all()则返回所有行:
# host = session.query(Host).filter(Host.hostname == 'aaa').one()
# print(host.id, host.hostname, host.ip_addr, host.port, )






# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# # 创建数据库引擎
# engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test", echo=True)
# # 生成一个SqlORM 基类
# Base = declarative_base()
# # 定义表结构
# class User(Base):
#     # 表名
#     __tablename__ = 'users'
#     # 定义id,主键唯一,
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
# # 寻找Base的所有子类，按照子类的结构在数据库中生成对应的数据表信息
# Base.metadata.create_all(engine)
# # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
# Session = sessionmaker(bind=engine)
# session = Session()
# # 获取session，然后把对象添加到session，
# # 最后提交并关闭。Session对象可视为当前数据库连接。


# 一对多
# from sqlalchemy import create_engine, func
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import sessionmaker, relationship
#
# # 生成sqlorm基类
# Base = declarative_base()
# # 创建数据库连接
# engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test?charset=utf8", encoding="utf-8", echo=True)
# # 目的是一个人可以拥有多本书，那么在数据库里的一对多关系
#
#
# class User(Base):
#     # 表名
#     __tablename__ = 'user'
#     # id字段
#     id = Column(String(20), primary_key=True)
#     # 名字字段
#     name = Column(String(20))
#     '''
#     内容不是表名而是定义的表结构名字,与生成表结构无关，仅用于查询方便,
#     例如: User.books可以连接到 Book表详细调用情况请看最后例子.
#     '''
#     books = relationship('Book', backref='u')
#
#
# class Book(Base):
#     # 表名
#     __tablename__ = 'book'
#     # id字段
#     id = Column(String(20), primary_key=True)
#     # 名字字段
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     # ForeignKey是外键 关联user表的id字段
#     user_id = Column(String(20), ForeignKey('user.id'))
#
# # 创建所有表结构
# Base.metadata.create_all(engine)
#
# if __name__ == '__main__':
#     # 绑定,生成会话
#     SessionCls = sessionmaker(bind=engine)
#     session = SessionCls()
#     # 创建用户
#     lianglian = User(id='1', name='lianglian')
#     jack = User(id='2', name='jack')
#     # 添加字段
#     session.add_all([lianglian, jack])
#     # 提交
#     session.commit()
#     # 创建白鹿原这本书，指定谁是拥有者
#     Whitedeer = Book(id='1', name='White_deer', user_id='1')
#     # 创建三体这本书，指定谁是拥有者
#     Threebody1 = Book(id='2', name='Three_body', user_id='1')
#     Threebody2 = Book(id='3', name='Three_body', user_id='2')
#     La_traviata = Book(id='4', name='茶花女', user_id='2')
#     # 添加字段
#     session.add_all([Whitedeer, Threebody1, Threebody2, La_traviata])
#     # 提交
#     session.commit()
#
#
#     # 获取每个用户下面的书名称
#     ret = session.query(User).filter_by(name='lianglian').first()
#     for i in ret.books:
#         print(i.name)
#
#     ret = session.query(User).filter_by(name='jack').first()
#     for i in ret.books:
#         print(i.name)
#
#     # 获取这本书谁看过,
#     ret = session.query(Book).filter(Book.name == "Three_body").all()
#     for i in ret.u:
#         print(i.u.name)
#
#
#     '''
#     上面的例子,就是加了一个books属性relationship指定了User和Book表结构之间的关系,可以相互快速的查询对应的内容,通过这个books去查询叫做正向查询
#
#     backref='u',表示Book表结构中可以通过backref中指定的u关键字查询User表中的数据.通过'u'去查询的方式叫做反向查询.
#     '''


# from sqlalchemy import Column, Sequence, String, Integer, ForeignKey
# from sqlalchemy import create_engine   # 导入创建连接驱动
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import relationship, backref
#
# engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/test?charset=utf8", encoding="utf-8", echo=True)
# # 生成了declarative基类, 以后的model继承此类
# Base = declarative_base()
#
#
# class Hosts(Base):
#     __tablename__ = 'hosts'
#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     name = Column(String(64), unique=True, nullable=False)
#     ip_addr = Column(String(128), unique=True, nullable=False)
#     port = Column(Integer, default=22)
#     group_id = Column(Integer, ForeignKey('group.id'))
#     group_re = relationship("Group", back_populates="hosts_re")
#
# class Group(Base):
#     __tablename__ = 'group'
#     id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
#     name = Column(String(64), unique=True, nullable=False)
#     hosts_re = relationship("Hosts", back_populates="group_re")
#
# Base.metadata.create_all(engine)   # 创建所有表结构
#
# if __name__ == '__main__':
#     SessionCls = sessionmaker(bind=engine)
#     # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
#     session = SessionCls()
#     g1 = Group(name='g1')
#     g2 = Group(name='g2')
#     a1 = Hosts(name='a1', ip_addr='1.1.1.1', group_id=1)
#     a2 = Hosts(name='a2', ip_addr='2.2.2.2', group_id=1)
#     b1 = Hosts(name='b1', ip_addr='3.3.3.3', group_id=2)
#     b2 = Hosts(name='b2', ip_addr='4.4.4.4', group_id=2)
#     session.add_all([g1, g2, a1, a2, b1, b2])
#     session.commit()
#
#     # 查询主机组
#     ret = session.query(Hosts).filter(Hosts.name == "a1").all()
#     for i in ret:
#         print(i.group_re.name)
#
#     # 从主机组中查询主机
#     ret = session.query(Group).filter(Group.name == "g1").all()
#     for i in ret:
#         for h in i.hosts_re:
#             print(h.name)




# 多对多
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

    # 外键,建立两个表中数据与数据对应关系,正向通过这个表这个字段可以找到host表中的nid对于
    host_id = Column(Integer, ForeignKey('host.nid'))
    # 外键,建立两个表中数据与数据对应关系,正向通过这个表这个字段可以找到host_user表中的nid对应
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

    # 间接建立关联,基于通过HostToHostUser表找到HostUser表结构的关联关系上建立我这个Host表直接与HostUser表的关联关系,
    # 这里有backref,你猜猜能不能从HostUser反向查询?? 答案是可以的! 通过关系表搭桥找到你心中的那个她~
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


session.add_all([
    Host(hostname='c1',port='22',ip='1.1.1.1'),
    Host(hostname='c2',port='22',ip='1.1.1.2'),
    Host(hostname='c3',port='22',ip='1.1.1.3'),
    Host(hostname='c4',port='22',ip='1.1.1.4'),
    Host(hostname='c5',port='22',ip='1.1.1.5'),
])
session.commit()


session.add_all([
    HostUser(username='root'),
    HostUser(username='db'),
    HostUser(username='nb'),
    HostUser(username='sb'),
])
# 提交修改
session.commit()

session.add_all([
    HostToHostUser(host_id=1,host_user_id=1),
    HostToHostUser(host_id=1,host_user_id=2),
    HostToHostUser(host_id=1,host_user_id=3),
    HostToHostUser(host_id=2,host_user_id=2),
    HostToHostUser(host_id=2,host_user_id=4),
    HostToHostUser(host_id=2,host_user_id=3),
])
session.commit()

# 获取主机1中所有用户
# 传统方法
# 查询Host表中hostname等于'c1'的,等到匹配数据的Host类对象(因为那一行是用Host类创建的)
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
# 查询HostToHostUser表结构中host_id == 1(host表中'c1'主机的nid)得到对应的host_user_id
host_2_host_user = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == host_obj.nid).all()

r = zip(*host_2_host_user)  # 将得到的host_user_id数据去掉list中的元祖
users = session.query(HostUser.username).filter(HostUser.nid.in_(list(r)[0])).all()
print(users)


# 新方法
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
# 通过反向查找找到关系关联表,然后通过关系表中与host_user关联直接便可得到host_user表中相应的数据
for item in host_obj.h:
    print(item.host_user.username)

# 走Host表通过HostToHostUser搭桥建立的关联关系正向查询
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
for item in host_obj.host_user:
    print(item.username)

# 走Host表通过HostToHostUser搭桥建立的关联关系反向查询
host_obj = session.query(HostUser).filter(HostUser.username == 'nb').first()
for item in host_obj.h:
    print(item.hostname)
