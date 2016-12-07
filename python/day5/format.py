#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

# 当格式化字符串时,如果出现占位符% 显示需要写%%,没有占位符写几个%就是几个%号


# tp1 = "i am {}, age{}, {}".format("seven", 18, 'alex')
# tp1 = "i am {}, age{}, {}".format(*["seven", 18, 'alex'])
# tp1 = "i am {0}, age{1}, {0}".format("seven", 18, )
# tp1 = "i am {0}, age{1}, {0}".format(*["seven", 18, ])
# tp1 = "i am {name}, age{age}, {name}".format(name="seven", age=18, )
# tp1 = "i am {name}, age{age}, {name}".format(**{'name': 'seven', 'age': '18'})
# tp1 = "i am {0[0]}, age{0[1]}, {0[2]}".format([1,2,3], [4,5,6])
# tp1 = "i am {:s}, age{:d}, {:f}".format('seven', 18, 888888.1)
# tp1 = "i am {name:s}, age{age:d}, ".format(name="seven", age=18, )
# tp1 = "i am {name:s}, age{age:d}, ".format(**{'name': 'seven', 'age': 18})
# tp1 = "numbers: {:b},{:o},{:d},{:x},{:X},{:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
# tp1 = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
# tp1 = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

# 没有指定格式化规则,默认按照参数顺序填充
tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')

# format方法采用动态参数,接受序列参数*[]遍历序列传递
tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])

# 指定格式化参数位置
tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])

# 指定格式化名称,参数以key-value形式传递,对应指定名称传递参数
tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)

# format方法采用动态参数,接受序列参数**{}遍历序列传递
tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})

# 参数序列索引传递
tpl = "i am {0[0]}, age {0[1]}, really {1[2]}".format([1, 2, 3], [11, 22, 33])

# 指定格式化类型
tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
tpl = "i am {:s}, age {:d}".format(*["seven", 18])
tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})

# 格式化类型
tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

# 宽度30字符居中,用"-"填充
tpl = "{:-^30}".format("居中")



print(tpl)