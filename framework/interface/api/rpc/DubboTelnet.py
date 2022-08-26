#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author: jayzhen
@email: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm & Python 2.7
@file: DubboTelnet.py 
@time: 2018/09/14 13:28 
"""


import dubbo_telnet


def coondoubble_data(Host,Port,interface,method,param):
    try:
        # 初始化dubbo对象
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(10)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('gbk')
        conn.invoke(interface, method, param)
        command = 'invoke %s.%s(%s)'%(interface,method,param)
        return conn.do(command)
    except:
        return Exception


if __name__ == "__main__":
    Host = '*.*.*.*'  # Doubble服务器IP
    Port = 20887  # Doubble服务端口
    interface = 'com.auto.Interface.*'  # 接口
    method = 'getAllfunctioninfo'  # 方法
    param = ''  # 参数
    data = coondoubble_data(Host,Port,interface,method,param)
    print data
