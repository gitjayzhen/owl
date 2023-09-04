# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: mysql_client.py
@time: 2023/9/4 18:58
"""

from concurrent.futures import ThreadPoolExecutor

import mysql.connector
import pymysql
from DBUtils.PooledDB import PooledDB

from owl.lib.decorator import singleton


@singleton
class MySQLConnection:

    def __init__(self):
        self.connection = None
        self.thread_pool = ThreadPoolExecutor(max_workers=5)  # 创建一个最大容纳5个线程的线程池

    def connect(self):
        self.connection = mysql.connector.connect(
            host='127.0.0.1',  # 服务器地址
            port=3306,  # 端口号，默认是3306
            user='root',  # 要登陆的用户名
            passwd='root',  # 所要登录用户的秘密
            db='test_db',  # 所要链接的数据库
            charset='utf-8'  # 设置链接的编码
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


class MySQLConnectionPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            db_pool = PooledDB(
                creator=pymysql,
                maxconnections=5,
                host='your_host',
                user='your_username',
                password='your_password',
                database='your_database'
            )
            cls._instance.db_pool = db_pool
        return cls._instance

    def get_connection(self):
        return self.db_pool.connection()
