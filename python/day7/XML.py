#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Liang Lian


# 查看
# from xml.etree import ElementTree as ET
#
# tree = ET.parse('data.xml')
# tree_root = tree.getroot()
# print(tree_root)  # 返回的是Element的一个可被迭代的数据对象
#
# for child in tree_root:    #
#     print(child.tag, child.attrib)  # 查看这个标签和属性
#     for gradechild in child:
#         print(gradechild.tag, gradechild.text)


# # 解析字符串修改保存
# from xml.etree import ElementTree as ET
#
# str_xml = open('./data.xml', 'r').read()
#
# root = ET.XML(str_xml)
#
# # print(root.tag)
#
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#
#     node.set('name', 'SB')
#     node.set('age', '18')
#
#     del node.attrib['name']
#
#
# ############ 保存文件 ############
# tree = ET.ElementTree(root)
# tree.write("new.xml", encoding='utf-8')


# # 解析文件修改保存
# from xml.etree import ElementTree as ET
#
# str_xml = open('./data.xml', 'r').read()
#
# root = ET.XML(str_xml)
#
# # print(root.tag)
#
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#
#     node.set('name', 'SB')
#     node.set('age', '18')
#
#     del node.attrib['name']
#
#
# ############ 保存文件 ############
# tree = ET.ElementTree(root)
# tree.write("new.xml", encoding='utf-8')




# from xml.etree import ElementTree as ET
#
# ############ 解析方式一 ############
# """
# # 打开文件，读取XML内容
# str_xml = open('data.xml', 'r').read()
#
# # 将字符串解析成xml特殊对象，root代指xml文件的根节点
# root = ET.XML(str_xml)
# """
# ############ 解析方式二 ############
#
# # 直接解析xml文件
# tree = ET.parse("data.xml")
#
# # 获取xml文件的根节点
# root = tree.getroot()
#
#
# ### 操作
#
# # 顶层标签
# print(root.tag)
#
#
# # 遍历XML文档的第二层
# for child in root:
#     # 第二层节点的标签名称和标签属性
#     print(child.tag, child.attrib)
#     # 遍历XML文档的第三层
#     for i in child:
#         # 第二层节点的标签名称和内容
#         print(i.tag, i.text)



# from xml.etree import ElementTree as ET
#
# ############ 解析方式一 ############
# """
# # 打开文件，读取XML内容
# str_xml = open('data.xml', 'r').read()
#
# # 将字符串解析成xml特殊对象，root代指xml文件的根节点
# root = ET.XML(str_xml)
# """
# ############ 解析方式二 ############
#
# # 直接解析xml文件
# tree = ET.parse("data.xml")
#
# # 获取xml文件的根节点
# root = tree.getroot()
#
#
# ### 操作
#
# # 顶层标签
# print(root.tag)
#
#
# # 遍历XML中所有的year节点
# for node in root.iter('year'):
#     # 节点的标签名称和内容
#     print(node.tag, node.text)



# from xml.etree import ElementTree as ET
#
# ############ 解析方式一 ############
#
# # 打开文件，读取XML内容
# str_xml = open('data.xml', 'r').read()
#
# # 将字符串解析成xml特殊对象，root代指xml文件的根节点
# root = ET.XML(str_xml)
#
# ############ 操作 ############
#
# # 顶层标签
# print(root.tag)
#
# # 循环所有的year节点
# for node in root.iter('year'):
#     # 将year节点中的内容自增一
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#
#     # 设置属性
#     node.set('name', 'alex')
#     node.set('age', '18')
#     # 删除属性
#     del node.attrib['name']
#
#
# ############ 保存文件 ############
# tree = ET.ElementTree(root)
# tree.write("newnew.xml", encoding='utf-8')



# from xml.etree import ElementTree as ET
#
# ############ 解析方式二 ############
#
# # 直接解析xml文件
# tree = ET.parse("data.xml")
#
# # 获取xml文件的根节点
# root = tree.getroot()
#
# ############ 操作 ############
#
# # 顶层标签
# print(root.tag)
#
# # 循环所有的year节点
# for node in root.iter('year'):
#     # 将year节点中的内容自增一
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#
#     # 设置属性
#     node.set('name', 'alex')
#     node.set('age', '18')
#     # 删除属性
#     del node.attrib['name']
#
#
# ############ 保存文件 ############
# tree.write("newnew.xml", encoding='utf-8')



# from xml.etree import ElementTree as ET
#
# ############ 解析字符串方式打开 ############
#
# # 打开文件，读取XML内容
# str_xml = open('data.xml', 'r').read()
#
# # 将字符串解析成xml特殊对象，root代指xml文件的根节点
# root = ET.XML(str_xml)
#
# ############ 操作 ############
#
# # 顶层标签
# print(root.tag)
#
# # 遍历data下的所有country节点
# for country in root.findall('country'):
#     # 获取每一个country节点下rank节点的内容
#     rank = int(country.find('rank').text)
#
#     if rank > 50:
#         # 删除指定country节点
#         root.remove(country)
#
# ############ 保存文件 ############
# tree = ET.ElementTree(root)
# tree.write("newnew.xml", encoding='utf-8')



# from xml.etree import ElementTree as ET
#
# ############ 解析文件方式 ############
#
# # 直接解析xml文件
# tree = ET.parse("data.xml")
#
# # 获取xml文件的根节点
# root = tree.getroot()
#
# ############ 操作 ############
#
# # 顶层标签
# print(root.tag)
#
# # 遍历data下的所有country节点
# for country in root.findall('country'):
#     # 获取每一个country节点下rank节点的内容
#     rank = int(country.find('rank').text)
#
#     if rank > 50:
#         # 删除指定country节点
#         root.remove(country)
#
# ############ 保存文件 ############
# tree.write("newnew.xml", encoding='utf-8')



# from xml.etree import ElementTree as ET
#
#
# # 创建根节点
# root = ET.Element("famliy")
#
#
# # 创建节点大儿子
# son1 = ET.Element('son', {'name': '儿1'})
# # 创建小儿子
# son2 = ET.Element('son', {"name": '儿2'})
#
# # 在大儿子中创建两个孙子
# grandson1 = ET.Element('grandson', {'name': '儿11'})
# grandson2 = ET.Element('grandson', {'name': '儿12'})
# son1.append(grandson1)
# son1.append(grandson2)
#
#
# # 把儿子添加到根节点中
# root.append(son1)
# root.append(son1)
#
# tree = ET.ElementTree(root)
# tree.write('old.xml',encoding='utf-8', short_empty_elements=False)



# from xml.etree import ElementTree as ET
#
# # 创建根节点
# root = ET.Element("famliy")
#
#
# # 创建大儿子
# # son1 = ET.Element('son', {'name': '儿1'})
# son1 = root.makeelement('son', {'name': '儿1'})
# # 创建小儿子
# # son2 = ET.Element('son', {"name": '儿2'})
# son2 = root.makeelement('son', {"name": '儿2'})
#
# # 在大儿子中创建两个孙子
# # grandson1 = ET.Element('grandson', {'name': '儿11'})
# grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# # grandson2 = ET.Element('grandson', {'name': '儿12'})
# grandson2 = son1.makeelement('grandson', {'name': '儿12'})
#
# son1.append(grandson1)
# son1.append(grandson2)
#
#
# # 把儿子添加到根节点中
# root.append(son1)
# root.append(son1)
#
# tree = ET.ElementTree(root)
# tree.write('old.xml',encoding='utf-8', short_empty_elements=False)


# from xml.etree import ElementTree as ET
#
#
# # 创建根节点
# root = ET.Element("famliy")
#
#
# # 创建节点大儿子
# son1 = ET.SubElement(root, "son", attrib={'name': '儿1'})
# # 创建小儿子
# son2 = ET.SubElement(root, "son", attrib={"name": "儿2"})
#
# # 在大儿子中创建一个孙子
# grandson1 = ET.SubElement(son1, "age", attrib={'name': '儿11'})
# grandson1.text = '孙子'
#
#
# et = ET.ElementTree(root)  #生成文档对象
# et.write("test.xml", encoding="utf-8", xml_declaration=True, short_empty_elements=False)



# from xml.etree import ElementTree as ET
# from xml.dom import minidom
#
#
# def prettify(elem):
#     """将节点转换成字符串，并添加缩进。
#     """
#     rough_string = ET.tostring(elem, 'utf-8')
#     reparsed = minidom.parseString(rough_string)
#     return reparsed.toprettyxml(indent="\t")
#
# # 创建根节点
# root = ET.Element("famliy")
#
#
# # 创建大儿子
# # son1 = ET.Element('son', {'name': '儿1'})
# son1 = root.makeelement('son', {'name': '儿1'})
# # 创建小儿子
# # son2 = ET.Element('son', {"name": '儿2'})
# son2 = root.makeelement('son', {"name": '儿2'})
#
# # 在大儿子中创建两个孙子
# # grandson1 = ET.Element('grandson', {'name': '儿11'})
# grandson1 = son1.makeelement('grandson', {'name': '儿11'})
# # grandson2 = ET.Element('grandson', {'name': '儿12'})
# grandson2 = son1.makeelement('grandson', {'name': '儿12'})
#
# son1.append(grandson1)
# son1.append(grandson2)
#
#
# # 把儿子添加到根节点中
# root.append(son1)
# root.append(son1)
#
#
# raw_str = prettify(root)
#
# f = open("xxxoo.xml",'w',encoding='utf-8')
# f.write(raw_str)
# f.close()


from xml.etree import ElementTree as ET

ET.register_namespace('com',"http://www.company.com") #some name

# build a tree structure
root = ET.Element("{http://www.company.com}STUFF")
body = ET.SubElement(root, "{http://www.company.com}MORE_STUFF", attrib={"{http://www.company.com}hhh": "123"})
body.text = "STUFF EVERYWHERE!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)

tree.write("page.xml",
           xml_declaration=True,
           encoding='utf-8',
           method="xml")