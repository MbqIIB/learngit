#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

class C1:

    def f1(self):
        print('c1.f1')

class C2(C1):

    def f1(self):
        #主动执行父类的f1方法
        super(C2,self).f1()
        print('c2.f1')

        # C1.f1(self)

obj = C2()
obj.f1()