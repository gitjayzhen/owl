# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: redis_client.py
@time: 2023/9/4 16:53
"""

import redis
from redis.connection import ConnectionPool

from owl.configs import ConfigReader
from owl.exception.owl_type import SingletonInstantiationException


class RedisSingleton:
    __instance = None

    @staticmethod
    def get_instance():
        if not RedisSingleton.__instance:
            RedisSingleton()
        return RedisSingleton.__instance

    def __init__(self):
        if RedisSingleton.__instance:
            raise SingletonInstantiationException()
        else:
            RedisSingleton.__instance = self
            # 获取Redis连接配置
            redis_config = ConfigReader().get_redis_config()

            # 创建连接池对象
            self.pool = ConnectionPool(
                host=redis_config['host'],
                port=redis_config['port'],
                db=redis_config['db'],
                password=redis_config['passwd']
            )
            # 创建连接池 host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
            # 创建Redis客户端对象，并指定连接池
            self.client = redis.Redis(connection_pool=self.pool, decode_responses=True)
