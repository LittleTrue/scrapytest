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
# spidertest.py
# @author LittleTrue(GXZ)
# @email: 644812368@qq.com
# @website: www.jianshu.com/u/8775ddf16c8b
# @department : personal Development
# @module_description : 爬虫requests库测试,用户代理,ip代理技术测试
# @created Thu Oct 11 2018 00:05:27 GMT+0800 (中国标准时间)
# @last-modified Sun Oct 14 2018 23:45:43 GMT+0800 (中国标准时间)
# @copyright © 2018- personal All Rights Reserved.
import requests

# 发送一个post
# 超时 你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应
timeout = 1
# 定制请求头,比如设置伪装的用户代理
headers = {
    'User-Agent': 'Mozilla/4.0(compatible; MSIE 8.0; Windows NT 6.0',
    "Cookie": 'Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177;'
}
# 发起一个带参post
#payload = {'key1': 'value1', 'key2': 'value2'}

proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
r = requests.post(
    'https://www.cnblogs.com',
    #params=payload,
    timeout=timeout,
    headers=headers,
    # proxies=proxies,
)
# 输出请求状态码
print(r.status_code)

# Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码。
# 请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。
# 当你访问 r.text 之时，Requests 会使用其推测的文本编码。你可以找出 Requests 使用了什么编码，
# 并且能够使用 r.encoding 属性来改变它：
r.encoding = 'gbk'
print(r.text)
print(r.json())

# 快速访问cookie
r.cookies['example_cookie_name']
# 设置代理ip
