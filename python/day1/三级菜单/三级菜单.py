#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian

map_dict = {
    '北京市': {
        '海淀区': ['中关村', '安贞', '西直门', '西苑'],
        '东城区': ['东直门', '王府井', '灯市口', '东四'],
        '朝阳区': ['呼家楼', '十里堡', '四惠', '燕莎', '亮马桥'],
        '丰台区': ['宋家庄', '大红门', '角门', '陶然亭']
    },
    '上海市': {
        '浦东新区': ['金桥', '洋泾', '塘桥', '八佰伴'],
        '黄浦区': ['外滩', '南京东路', '董家渡', '江宁路'],
        '虹口区': ['提篮桥', '长阳路', '临平路', '四平路'],
        '普陀区': ['长征', '真如', '梅川路', '金沙江路']
    },
    '广东省': {
        '广州市': {
            '天河区': ['石碑', '跑马场', '员村', '天园'],
            '海珠区': ['新港', '赤岗', '瑞宝', '南洲'],
            '白云区': ['三元里', '广园路', '流花', '捞金'],
        },
        '深圳市': {
            '罗湖区': ['圆领', '东门', '黄贝岭', '翠竹'],
            '宝安区': ['西乡', '新安', '南头', '科技园'],
            '福田区': ['赤尾', '黄冈', '东宫庙', '福华新村']
        }
    },
    '湖南省': {
        '长沙市': {
            '雨花区': ['香樟路', '树木岭', '圭塘', '韶山南路'],
            '天心区': ['新开铺', '友谊路', '红星村', '井湾子'],
            '芙蓉区': ['杨家山', '凌霄路', '文艺路', '湘湖'],
            },
        '衡阳市': {
            '雁峰区': ['衡州大道', '蒸湘北路', '蔡伦大道'],
            '珠晖区': ['船山大道', '湘江北路', '东风路'],
            '石鼓区': ['蔡伦大道', '华源大道', '宋海村']
        }
    }
}


flag = True
while flag:  # 设置可调节循环的条件,方便在程序中控制
    print("---------中国省市地区查询系统------------")
    province_list = list(map_dict.keys())   # 字典的keys()方法得到字典的key 放入列表(有序化)
    for index, province in enumerate(province_list, 1):  # enumerate()函数挺好用的,遍历打印数字序号
        print(index, province)      # 打印列表一级菜单
    province_input = input("请输入菜单序号进行下一步查询,也可按q退出:")
    if province_input == 'q':
        print("欢迎使用中国省市地区查询系统,拜拜!")
        break
    elif province_input.isdigit() and int(province_input) <= len(province_list):  # 判断用户输入是数字,并且数字小于等于列表长度
        province_input = int(province_input)-1  # 通过对list索引获取key值(用户输入和列表索引差1,所以减1)
        provinciale_key = province_list[province_input]  # 得到有序列表是为了在这里使用,得到用户输入变成list index从list中取出用户想要的.
        provinciale_list = list(map_dict[provinciale_key].keys())  # 通过一级key,得到二级字典
        while flag:
            for index, provinciale in enumerate(provinciale_list, 1):
                print(index, provinciale)   # 打印列表二级菜单
            provinciale_input = input("请输入菜单序号进行下一步查询,也可按q退出,按b返回:")
            if provinciale_input == "b":
                break
            elif provinciale_input == "q":
                print("欢迎使用中国省市地区查询系统,拜拜!")
                flag = False   # 重设循环条件,设置成False 让父循环跳出(一级循环)
                break          # 跳出本次循环,(二级循环)
            elif provinciale_input.isdigit() and int(provinciale_input) <= len(provinciale_list) :
                provinciale_input = int(provinciale_input)-1  # 通过对list索引获取key值(用户输入和列表索引差1,所以减1)
                region_key = provinciale_list[provinciale_input]
                if type(map_dict[provinciale_key][region_key]) == list :  # 判断是否是list,如果是则说明是最后一层了,如果不是则继续
                    region_list = map_dict[provinciale_key][region_key]   # 通过二级key,得到三级列表
                    while flag:
                        for index, region in enumerate(region_list, 1):
                            print(index, region)    # 打印列表三级菜单
                        end_input = input("按q退出, 按b返回:")
                        if end_input == "b":
                            break
                        elif end_input == "q":
                            print("欢迎使用中国省市地区查询系统,拜拜!")
                            flag = False    # 重设循环条件,设置成False来跳出循环(二级循环)
                            break           # 跳出本次循环,(三级循环)
                elif type(map_dict[provinciale_key][region_key]) == dict:
                    while flag:
                        region_list = list(map_dict[provinciale_key][region_key].keys())  # 通过二级key,得到三级字典
                        for index, region in enumerate(region_list, 1):
                            print(index, region)    # 打印列表三级菜单
                        region_input = input("请输入菜单序号进行下一步查询,也可按q退出,按b返回:")
                        if region_input == "b":
                            break
                        elif region_input == "q":
                            print("欢迎使用中国省市地区查询系统,拜拜!")
                            flag = False    # 重设循环条件,设置成False来跳出循环(二级循环)
                            break           # 跳出本次循环,(三级循环)
                        elif region_input.isdigit() and int(region_input) <= len(region_list):
                            region_input = int(region_input) - 1  # 通过对list索引获取key值(用户输入和列表索引差1,所以减1)
                            place_key = region_list[region_input]
                            if type(map_dict[provinciale_key][region_key][place_key]) == list:  # 判断是否市list
                                place_list = map_dict[provinciale_key][region_key][place_key]  # 通过三级key,得到四级列表
                                while flag:
                                    for index, place in enumerate(place_list, 1):
                                        print(index, place)
                                    end_input = input("按q退出, 按b返回:")
                                    if end_input == "b":
                                        break
                                    elif end_input == "q":
                                        print("欢迎使用中国省市地区查询系统,拜拜!")
                                        flag = False    # 重设循环条件,设置成False来跳出循环(三级循环)
                                        break           # 跳出本次循环,(四级循环)
                                    else:
                                        print("您的输入有误,请按照提示重新输入!")
                        else:
                            print("您的输入有误,请按照提示重新输入!")
            else:
                print("您的输入有误,请按照提示重新输入!")
    else:
        print("您的输入有误,请按照提示重新输入!")
