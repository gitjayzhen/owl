# -*- coding=utf-8 -*-
'''
Created on 2017年11月21日

@author: jayzhen
pip install redis 官网推荐
'''


import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

r = redis.Redis(host='10.150.20.*', port=6379, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
# r.set('name', 'junxi')  # key是"foo" value是"bar" 将键值对存入redis缓存
# print(r['name'])
print(r.get('app:register:sendsms:count:14511111111'))  # 取出键name对应的值
print(type(r.get('name')))


def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)

# 使用
for item in list_iter('list2'):  # 遍历这个列表
    print(item)
