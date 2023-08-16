#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'jayzhen'

# 定义结构体,最好继承object，不让有些方法无法使用


class DataStruct(object):

    """
      于接收读取的测试数据,记录要写入测试报告的数据
      数据驱动，作为数据的标准输入，不管数据是通过excel、txt、configs、sql等方式表现，到了这里，都将是接口所需的标准类型json|xml等
    """

    def __init__(self):
        self.cid = 0                    # 用例ID
        self.project = None            # 接口所在的项目名
        self.module = None             # 接口所在的模块名
        self.function = None               # 接口对应的功能点
        self.desc = None              # 测试(用力)描述
        self.type = 0                  # 表示接口还是网页：0是网页  1是接口 这个场景是接口还是web请求；如果是接口断言处理的方式是模板式数据处理；如果是网页请求那就按网络爬虫处理
        self.protocol = None            # 协议
        self.url = None                 # 接口请求url
        self.method = None              # 接口请求方法
        self.header = None              # 接口的header
        self.cookie = None              # 请求参数
        self.entity = None              # 接口的实体
        self.assertion = None             # 接口需要校验的内容
        self.result = None             # 测试结果(status、responed、assetresult、testresult)
        self.notes = None             # 失败原因



