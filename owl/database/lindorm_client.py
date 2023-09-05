# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: lindorm_client.py
@time: 2023/9/5 10:29
"""

from dbutils.pooled_db import PooledDB
import importlib


class DBUtilsDemo:

    def __init__(self, url, user, password, database):
        config = {
            'url': url,
            'lindorm_user': user,
            'lindorm_password': password,
            'database': database,
            'autocommit': True
        }
        db_creator = importlib.import_module("phoenixdb")
        # 基于DBUtils的连接池
        self.pooled = PooledDB(db_creator,
                               maxcached=10,
                               # 连接池的最大空闲连接数,可以根据实际需要调整
                               maxconnections=50,
                               # 连接池的最大连接数, 可以根据实际需要调整
                               blocking=True,
                               # 如果连接池没有空闲的连接，是否等待。True：等待空闲连接；False：不等待并报错。
                               ping=1,
                               # 检查服务端是否可用
                               **config)

    # 从连接池获取连接
    def _connect(self):
        try:
            r = self.pooled.connection()
            return r
        except Exception as e:
            print("Failed to connect:" + str(e))

    # 归还连接到连接池
    def _close(self, conn, stmt):
        if stmt:
            stmt.close()
        if conn:
            conn.close()

    # 查询单条记录
    def select_row(self, sql):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            statement.execute(sql)
            row = statement.fetchone()
            return row
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)

    # 查询多条记录
    def select_rows(self, sql):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            print(sql)
            statement.execute(sql)
            rows = statement.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)

    # 更新与插入
    def upsert_data(self, sql_upsert):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            statement.execute(sql_upsert)
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)

    # 更新与插入带参数
    def upsert_data_prams(self, sql_upsert, prams):
        connection = self._connect()
        statement = None
        try:
            statement = connection.cursor()
            statement.execute(sql_upsert, prams)
            connection.commit()
        except Exception as e:
            print(e)
        finally:
            self._close(connection, statement)

if __name__ == '__main__':
    # Lindorm 宽表SQL连接地址。
    url = 'http://ld-bp1p7e07ohamf****-proxy-lindorm-pub.lindorm.rds.aliyuncs.com:30060'
    # 用户名，根据实际情况做替换。您可以通过Lindorm集群管理系统查看用户名和密码。
    user = 'root'
    # 密码，根据实际情况做替换
    password = 'root'
    # 连接的数据库名称，根据实际情况做替换
    database = 'test'

    poolUtils = DBUtilsDemo(url, user, password, database)
    poolUtils.upsert_data("upsert into tb(id,name,address) values ('i001','n001','a001')")

    params = ['i002', 'n002', 'a002']
    poolUtils.upsert_data_prams("upsert into tb(id,name,address) values (?,?,?)", params)

    rows = poolUtils.select_rows("select * from tb")
    print(rows)

    row = poolUtils.select_row("select * from tb limit 1")
    print(row)

    row = poolUtils.select_row("select * from tb where id = 'i001' limit 1")
    print(row)