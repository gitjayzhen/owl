#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author: jayzhen
@software: PyCharm & Python 2.7
@file: DubboClientTest.py
@time: 2018/09/14 12:25 
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
