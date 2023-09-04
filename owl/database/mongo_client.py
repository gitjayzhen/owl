# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: mongo_client.py
@time: 2023/9/4 19:24
"""


import pymongo as pm


# pip install pymongo
# 单例模式
# 方法1,实现__new__方法
# 并在将一个类的实例绑定到类变量_instance上,
# 如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
# 如果cls._instance不为None,直接返回cls._instance


class Singleton(object):
    # 单例模式写法,参考：http://ghostfromheaven.iteye.com/blog/1562618
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MongoOperator(Singleton):
    def __init__(self, host, port, db_name, default_collection):
        """
        设置mongodb的地址，端口以及默认访问的集合，后续访问中如果不指定collection，则访问这个默认的
        :param host: 地址
        :param port: 端口
        :param db_name: 数据库名字
        :param default_collection: 默认的集合
        """
        #建立数据库连接
        self.client = pm.MongoClient(host=host, port=port)
        #选择相应的数据库名称
        self.db = self.client.get_database(db_name)
        #设置默认的集合
        self.collection = self.db.get_collection(default_collection)

    def insert(self, item, collection_name =None):
        """
        插入数据，这里的数据可以是一个，也可以是多个
        :param item: 需要插入的数据
        :param collection_name:  可选，需要访问哪个集合
        :return:
        """
        if collection_name is not None:
            collection = self.db.get_collection(self.db)
            collection.insert(item)
        else:
            self.collection.insert(item)

    def find(self, expression =None, collection_name=None):
        """
        进行简单查询，可以指定条件和集合
        :param expression: 查询条件，可以为空
        :param collection_name: 集合名称
        :return: 所有结果
        """
        if collection_name is not None:
            collection = self.db.get_collection(collection_name)
            if expression is None:
                return collection.find()
            else:
                return collection.find(expression)
        else:
            if expression is None:
                return self.collection.find()
            else:
                return self.collection.find(expression)

    def get_collection(self, collection_name=None):
        """
        很多时候单纯的查询不能够通过这个类封装的方法执行，这时候就可以直接获取到对应的collection进行操作
        :param collection_name: 集合名称
        :return: collection
        """
        if collection_name == None:
            return self.collection
        else:
            return self.get_collection(collection_name)


if __name__ == '__main__':
    db = MongoOperator('10.*.*.*', 27017, '*', 'mobileDataInfo')
    # item = {}
    # item['name'] = 'mebiuw'
    # item['age'] = '23'
    # db.insert(item)
    # for item in db.find():
    #     print(item)
    print(db.find(expression={'userId': 395}).next())
