# -*- coding: utf-8 -*-
# spider.py
# @author LittleTrue
# @email: 644812368@qq.com
# @website: www.jianshu.com/u/8775ddf16c8b
# @department : personal Development
# @module_description : 爬虫测试
# @created Tue Oct 09 2018 21:12:37 GMT+0800 (中国标准时间)
# @last-m·odified Tue Oct 09 2018 21:31:30 GMT+0800 (中国标准时间)
# @copyright personal
import requests

# 发送一个post
# 超时 你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应
timeout = 0.001
# 定制请求头,比如设置伪装的用户代理
headers = {
    'User-Agent':
    'Mozilla/4.0(compatible; MSIE 8.0; Windows NT 6.0',
    "Cookie":
    'Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036'
}
# 发起一个带参post
payload = {'key1': 'value1', 'key2': 'value2'}

proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}
r = requests.post(
    'https://api.github.com/events',
    params=payload,
    timeout=timeout,
    headers=headers,
    proxies=proxies,
)
# 输出请求状态码
r.status_code

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
