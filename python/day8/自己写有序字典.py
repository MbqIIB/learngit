#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

class MyDict(dict):

    def __init__(self):
        self.li = []
        super(MyDict, self).__init__()

    def __setitem__(self, key, value):
        self.li.append(key)
        super(MyDict, self).__setitem__(key,value)

    def __str__(self):
        dict_list = []

        for key in self.li:
            value = self.get(key)
            dict_list.append("'%s':%s" % (key,value))
        dict_str = "{" + ",".join(dict_list) + "}"
        return dict_str

obj = MyDict()
obj['k1'] = 123
obj['k2'] = 456
print(obj)




def func(self):
    print('hello wupeiqi')

Foo = type('Foo', (object,), {'func': func})
obj = Foo()
obj.func()

#type第一个参数：类名
#type第二个参数：当前类的基类
#type第三个参数：类的成员