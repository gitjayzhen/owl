# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license:  Apache Licence
@file: test_db.py
@time: 2023/9/4 15:28
"""

import pytest

from owl.database.mysql_client import MySQLConnection
from owl.database.redis_client import RedisSingleton


class TestRedisClient:

    def setup_class(cls):
        # 在类级别执行的设置操作
        cls.redis_instance = RedisSingleton.get_instance()

    def teardown_class(cls):
        # 在类级别执行的清理操作
        pass

    def setup_method(self, method):
        # 在每个测试方法之前执行的设置操作
        pass

    def teardown_method(self, method):
        # 在每个测试方法之后执行的清理操作
        pass

    def test_redis_connect(self):
        # pip install redis 官网推荐
        # 在其他地方获取Redis单例对象

        v = 'value12345'
        # 使用Redis客户端对象进行操作
        self.redis_instance.client.set('owl:test:key', v)
        result = self.redis_instance.client.get('owl:test:key')

        assert result.decode() == v

    def test_mysql_client(self):
        mysql_conn = MySQLConnection()
        mysql_conn.connect()

        result = mysql_conn.execute_query('SELECT * FROM your_table')
        print(result)

        result_async = mysql_conn.execute_query_async('SELECT * FROM your_table')
        print(result_async)

