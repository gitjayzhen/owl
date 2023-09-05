# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: mysql_client.py
@time: 2023/9/4 18:58

在Python中连接MySQL数据库有几个常用的库可以选择，包括：

1. **mysql-connector-python**：这是MySQL官方提供的Python驱动程序，支持Python 3，并且具有良好的性能和稳定性。你可以使用pip安装该库：`pip install mysql-connector-python`。

2. **pymysql**：这是一个纯Python实现的MySQL客户端库，兼容性好，可以用于连接MySQL服务器。你可以使用pip安装该库：`pip install pymysql`。

3. **MySQLdb**：这是Python 2.x版本中最常用的MySQL客户端库，但不支持Python 3.x版本。如果你正在使用Python 2.x，并且需要连接MySQL数据库，可以考虑使用MySQLdb。你可以使用pip安装该库：`pip install MySQL-python`。

4. **PyMySQLcursors**：这是pymysql库的一个扩展，提供了更多的游标类型和功能。你可以使用pip安装该库：`pip install PyMySQLcursors`。

以上这些库都可以用于连接和操作MySQL数据库。具体选择哪一个库取决于你的需求、Python版本以及个人偏好。请注意使用合适的库对应相应的Python版本，并根据文档和示例代码进行配置和使用。
"""

from concurrent.futures import ThreadPoolExecutor

import mysql.connector
import pymysql
from dbutils.pooled_db import PooledDB

from owl.configs import ConfigReader
from owl.lib.decorator import singleton


class MySQLConnection:
    _instance = None

    def __new__(cls, pool_name="owl_mysql", pool_size=5):
        if not cls._instance:
            cls._instance = super(MySQLConnection, cls).__new__(cls)
            cfg = ConfigReader.get_instance()
            db_config = cfg.get_mysql_config()
            cls._instance.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name=pool_name,
                                                                             pool_size=pool_size,
                                                                             **db_config)
        return cls._instance

    # def connect(self):
    #     cfg = ConfigReader().get_instance()
    #     param = cfg.get_mysql_config()
    #     self.connection = mysql.connector.connect(
    #         **param,
    #         db=param['database'],  # 所要链接的数据库
    #         charset='utf-8'  # 设置链接的编码
    #     )
    #
    # def execute_query(self, query):
    #     cursor = self.connection.cursor()
    #     cursor.execute(query)
    #     result = cursor.fetchall()
    #     cursor.close()
    #     return result

    def execute_query(self, query):
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def execute_queries(self, queries):
        with ThreadPoolExecutor(max_workers=self.pool.pool_size) as executor:
            futures = []
            for query in queries:
                future = executor.submit(self.execute_query, query)
                futures.append(future)

            results = []
            for future in futures:
                result = future.result()
                results.append(result)

        return results


class MySQLConnectionPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cfg = ConfigReader().get_redis_config()
            db_pool = PooledDB(
                creator=pymysql,
                maxconnections=5,
                **cfg.get_mysql_config()
            )
            cls._instance.db_pool = db_pool
        return cls._instance

    def get_connection(self):
        return self.db_pool.connection()
