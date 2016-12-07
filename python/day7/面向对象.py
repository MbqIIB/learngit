#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 类和对象
#     a.创建类
#         class 类名:
#
#             def 方法名(self,xxxx):
#                 pass
#     b.创建对象
#         对象 = 类名()
#
#     c.通过对象执行方法
#         对象.方法名()



# # 创建类
# class Foo:
#
#     def Bar(self):
#         print('Bar')
#
#     def Hello(self, name):
#         print('i am %s' % name)
#
# # 根据类Foo创建对象obj
# obj = Foo()
# obj.Bar()            # 执行Bar方法
# obj.Hello('lianglian')  # 执行Hello方法　


# >>> 什么时候使用面向对象编程 ?
#
# 当某一些函数具有相同参数时,可以使用面向对象的方法,将参数一次性封装到对象,以后去对象中取值

# self 是什么鬼 ?
#     >> self是一个python自动会传值的形式参数
#
#     obj1.fetch('select ...') self = obj1
#
#     obj2.fetch('select ...') self = obj2


# class Foo:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# obj1 = Foo('wupeiqi', 18)
# print(obj1.name)   # 直接调用obj1对象的name属性
# print(obj1.age)    # 直接调用obj1对象的age属性
#
# obj2 = Foo('alex', 73)
# print(obj2.name)    # 直接调用obj2对象的name属性
# print(obj2.age)     # 直接调用obj2对象的age属性



# class Foo:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def detail(self):
#         print(self.name)
#         print(self.age)
#
# obj1 = Foo('wupeiqi', 18)
# obj1.detail()  # Python默认会将obj1传给self参数，即：obj1.detail(obj1)，所以，此时方法内部的 self ＝ obj1，即：self.name 是 wupeiqi ；self.age 是 18
#
# obj2 = Foo('alex', 73)
# obj2.detail()  # Python默认会将obj2传给self参数，即：obj1.detail(obj2)，所以，此时方法内部的 self ＝ obj2，即：self.name 是 alex ； self.age 是 78



# def kanchai(name, age, gender):
#     print("%s,%s岁,%s,上山去砍柴" %(name, age, gender))
#
#
# def qudongbei(name, age, gender):
#     print("%s,%s岁,%s,开车去东北" %(name, age, gender))
#
#
# def dabaojian(name, age, gender):
#     print("%s,%s岁,%s,最爱大保健" %(name, age, gender))
#
#
# kanchai('小明', 10, '男')
# qudongbei('小明', 10, '男')
# dabaojian('小明', 10, '男')
#
#
# kanchai('老李', 90, '男')
# qudongbei('老李', 90, '男')
# dabaojian('老李', 90, '男')



# class Foo:
#
#     def __init__(self, name, age ,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def kanchai(self):
#         print("%s,%s岁,%s,上山去砍柴" %(self.name, self.age, self.gender))
#
#     def qudongbei(self):
#         print("%s,%s岁,%s,开车去东北" %(self.name, self.age, self.gender))
#
#     def dabaojian(self):
#         print("%s,%s岁,%s,最爱大保健" %(self.name, self.age, self.gender))
#
#
# xiaoming = Foo('小明', 10, '男')
# xiaoming.kanchai()
# xiaoming.qudongbei()
# xiaoming.dabaojian()
#
# laoli = Foo('老李', 90, '男')
# laoli.kanchai()
# laoli.qudongbei()
# laoli.dabaojian()









# # #####################  定义实现功能的类  #####################
#
# class Person:
#
#     def __init__(self, na, gen, age, fig):
#         self.name = na
#         self.gender = gen
#         self.age = age
#         self.fight =fig
#
#     def grassland(self):
#         """注释：草丛战斗，消耗200战斗力"""
#
#         self.fight -=200
#
#     def practice(self):
#         """注释：自我修炼，增长100战斗力"""
#
#         self.fight += 200
#
#     def incest(self):
#         """注释：多人游戏，消耗500战斗力"""
#
#         self.fight -= 500
#
#     def detail(self):
#         """注释：当前对象的详细情况"""
#
#         temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 战斗力:%s"  % (self.name, self.gender, self.age, self.fight)
#         print(temp)
#
#
# # #####################  开始游戏  #####################
#
# cang = Person('苍井井', '女', 18, 1000)    # 创建苍井井角色
# dong = Person('东尼木木', '男', 20, 1800)  # 创建东尼木木角色
# bo = Person('波多多', '女', 19, 2500)      # 创建波多多角色
#
# cang.incest()    # 苍井空参加一次多人游戏
# dong.practice()  # 东尼木木自我修炼了一次
# bo.grassland()   # 波多多参加一次草丛战斗
#
#
# #输出当前所有人的详细情况
# cang.detail()
# dong.detail()
# bo.detail()
#
#
# cang.incest()  # 苍井空又参加一次多人游戏
# dong.incest()  # 东尼木木也参加了一个多人游戏
# bo.practice()  # 波多多自我修炼了一次
#
# #输出当前所有人的详细情况
# cang.detail()
# dong.detail()
# bo.detail()





# 构造方法
# 类中有一个特殊的方法 __init__, 执行: 类名() 自动被执行


# 面向对象
# 三大特性: 封装,继承,多态


# # 函数式
#
# def fetch(host, username, password, sql):
#     pass
# def create(host, username, password, sql):
#     pass
# def remove(host, username, password, sql):
#     pass
# def modify(host, username, password, sql):
#     pass
#
#
# # 面向对象
# class SQLHelper:
#     def __init__(self, host, username, pwd):   # 构造方法
#         self.host = host
#         self.username = username
#         self.pwd = pwd
#
#     def fetch(self, sql):
#         pass
#     def create(self,sql):
#         pass
#     def remove(self,nid):
#         pass
#     def modify(self,name):
#         pass
#
# obj1 = SQLHelper('cl1.salt.com', 'lianglian', '123')
#
# obj1.fetch("select * from A")
#
# obj2 = SQLHelper('cl2.salt.com', 'lianglian', '123')
#
# obj2.fetch("select * from A")







# class 猫：
#
#     def 喵喵叫(self):
#         print('喵喵叫')
#
#     def 吃(self):
#         # do something
#
#     def 喝(self):
#         # do something
#
#     def 拉(self):
#         # do something
#
#     def 撒(self):
#         # do something
#
# class 狗：
#
#     def 汪汪叫(self):
#         print('汪汪叫')
#
#     def 吃(self):
#         # do something
#
#     def 喝(self):
#         # do something
#
#     def 拉(self):
#         # do something
#
#     def 撒(self):
#         # do something





# class 动物:
#
#     def 吃(self):
#         # do something
#
#     def 喝(self):
#         # do something
#
#     def 拉(self):
#         # do something
#
#     def 撒(self):
#         # do something
#
# # 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
# class 猫(动物)：
#
#     def 喵喵叫(self):
#         print('喵喵叫')
#
# # 在类后面括号中写入另外一个类名，表示当前类继承另外一个类
# class 狗(动物)：
#
#     def 汪汪叫(self):
#         print('汪汪叫')





# class Animal:
#
#     def eat(self):
#         print("%s 吃 " % self.name)
#
#     def drink(self):
#         print("%s 喝 " % self.name)
#
#     def shit(self):
#         print("%s 拉 " % self.name)
#
#     def pee(self):
#         print("%s 撒 " % self.name)
#
#
# class Cat(Animal):
#
#     def __init__(self, name):
#         self.name = name
#         self.breed = '猫'
#
#     def cry(self):
#         print('喵喵叫')
#
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#         self.breed = '狗'
#
#     def cry(self):
#         print('汪汪叫')
#
#
# # ######### 执行 #########
#
# c1 = Cat('小白家的小黑猫')
# c1.eat()
#
# c2 = Cat('小黑的小白猫')
# c2.drink()
#
# d1 = Dog('胖子家的小瘦狗')
# d1.eat()



# # 类嵌套
#
# class c1:
#     def __init__(self, name, obj):
#         self.name = name
#         self.obj = obj
#
#
# class c2:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(self.name)
#
#
# class c3:
#     def __init__(self,al):
#         self.money = 123
#         self.aaa = al
#
# c2_obj = c2('aa', '11')
# # c2_obj是c2类型
# # - name = "aa"
# # - age = 11
# c1_obj = c1('alex', c2_obj)
# # c1_obj 是c1 类型
# # - name = 'alex'
# # - obj = c2_obj
# c3_obj = c3(c1_obj)
# # 使用c3_obj执行show方法
#
# c2_obj.show()
# c3_obj.aaa.obj.show()




# # 类继承
# # 自己有的用自己的,自己没有的用父类的
# class F1:
#     def show(self):
#         print('show')
#
#     def foo(self):
#         print(self.name)
#
#
# class F2(F1):
#     def __init__(self, name):
#         self.name = name
#
#     def bar(self):
#         print("bar")
#
#     def show(self):
#         print("F2.show")
#
#
# obj = F2('alex')
# obj.foo()




# class F4:
#     def f4(self):
#         print('f4')
#
#
# class F3(F4):
#     def f3(self):
#         print('f3')
#
#
# class F2(F4):
#     def f2(self):
#         print('f2')
#
#
# class F1(F2, F3):
#     def f1(self):
#         print('f1')
#
# obj = F1()
# obj.f4()



# class F1:
#     pass
#
#
# class S1(F1):
#
#     def show(self):
#         print('S1.show')
#
#
# class S2(F1):
#
#     def show(self):
#         print('S2.show')
#
#
# # 由于在Java或C#中定义函数参数时，必须指定参数的类型
# # 为了让Func函数既可以执行S1对象的show方法，又可以执行S2对象的show方法，所以，定义了一个S1和S2类的父类
# # 而实际传入的参数是：S1对象和S2对象
#
# def Func(F1 obj):
#     """Func函数需要接收一个F1类型或者F1子类的类型"""
#
#     print(obj.show())
#
# s1_obj = S1()
# Func(s1_obj) # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show
#
# s2_obj = S2()
# Func(s2_obj) # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show




class F1:
    pass


# class S1(F1):
#
#     def show(self):
#         print('S1.show')
#
#
# class S2(F1):
#
#     def show(self):
#         print('S2.show')
#
#
# def Func(obj):
#     obj.show()
#
# s1_obj = S1()
# Func(s1_obj)
#
# s2_obj = S2()
# Func(s2_obj)
































