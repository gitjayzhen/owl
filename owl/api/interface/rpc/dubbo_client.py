# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: dubbo_client.py
@time: 2023/9/4 16:44
"""

import time


from dubbo_client import ApplicationConfig, ZookeeperRegistry, DubboClient

config = ApplicationConfig('test_rpclib')
service_interface = "com.auto.Interface.*"
# registry包含了和zookeeper的连接，该对象需要缓存
registry = ZookeeperRegistry('*.*.*.*:2181', config)
print(registry.get_provides(service_interface))
user_provider = DubboClient(service_interface, registry, version='2.5.3')
for i in range(100):
    print(user_provider("getAllfunctioninfo"))

    time.sleep(5)


def coondoubble_data(Host, Port, interface, method, param):
    try:
        # 初始化dubbo对象
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(10)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('gbk')
        conn.invoke(interface, method, param)
        command = 'invoke %s.%s(%s)' % (interface, method, param)
        return conn.do(command)
    except:
        return Exception


if __name__ == "__main__":
    Host = '*.*.*.*'  # Doubble服务器IP
    Port = 20887  # Doubble服务端口
    interface = 'com.auto.Interface.*'  # 接口
    method = 'getAllfunctioninfo'  # 方法
    param = ''  # 参数
    data = coondoubble_data(Host, Port, interface, method, param)
    print(data)
