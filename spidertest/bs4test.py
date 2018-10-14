# -*- coding: utf-8 -*-
#       ___           ___           ___
#      /\  \         |\__\         /\  \
#     /::\  \        |:|  |        \:\  \
#    /:/\:\  \       |:|  |         \:\  \
#   /:/  \:\  \      |:|__|__        \:\  \
#  /:/__/_\:\__\ ____/::::\__\ _______\:\__\
#  \:\  /\ \/__/ \::::/~~/~    \::::::::/__/
#   \:\ \:\__\    ~~|:|~~|      \:\~~\~~
#    \:\/:/  /      |:|  |       \:\  \
#     \::/  /       |:|  |        \:\__\
#      \/__/         \|__|         \/__/
# bs4test.py
# @author LittleTrue(GXZ)
# @email: 644812368@qq.com
# @website: www.jianshu.com/u/8775ddf16c8b
# @department : personal Development
# @module_description : 测试数据提取库bs4的使用
# @created Sun Oct 14 2018 23:22:41 GMT+0800 (中国标准时间)
# @last-modified Sun Oct 14 2018 23:58:43 GMT+0800 (中国标准时间)
# @copyright © 2018- personal All Rights Reserved.

from bs4 import BeautifulSoup 

html_doc = """
<html><head><title>The Dormouse's story<a>试试</a></title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
 
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
</ul>
 
<p class="story">...</p>
"""
# 得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出。
soup = BeautifulSoup(html_doc, 'html.parser')

# 获取网页内容
# print(soup.prettify())

# #获取网页的title
print(soup.title)

# 标准选择器find_all获取所有的a标签，并返回列表 find返回第一个
print(soup.findAll('a'))

# 获取class为story的p标签，且不能像find(id='**')来获取，因为class为python的关键字
print(soup.find('p', {'class': 'story'}).get_text())

# CSS选择器--通过select()直接传入CSS选择器就可以完成选择其中 .表示class #表示id
print(soup.select('#list-2 .element'))

# Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器
# 推荐使用lxml解析库，必要时使用html.parser
soup = BeautifulSoup(html_doc, "lxml")

# 总结:
# 标签选择筛选功能弱但是速度快
# 建议使用find()、find_all() 查询匹配单个结果或者多个结果
# 如果对CSS选择器熟悉建议使用select()
