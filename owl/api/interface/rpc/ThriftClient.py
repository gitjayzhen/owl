#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@message: jayzhen_testing@163.com
@file: demo_wencai_client.py
"""
import time
from unittest import TestCase

from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport


class TestWencai(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        host = "*.*.*.*"
        port = 8880

        tsocket = TSocket.TSocket(host, port)
        # transport = TTransport.TBufferedTransport(tsocket)
        self.transport = TTransport.TFramedTransport(tsocket)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        self.client = Client(self.protocol)
        self.transport.open()

    def tearDown(self):
        self.transport.close()

    def test_wc_new_article(self):
        """新发布的文章"""
        dta = Article()

        user = User()
        user.Uid = 115775
        user.Nickname = "jayzhen"

        # print chardet.detect("精选")

        dta.Id = 10006
        dta.Author = user
        dta.Type = 1
        dta.Title = "文采的后台thrift接口测试".decode("UTF-8")
        dta.SimpleContent = "文章内容列表页使用".decode("UTF-8")
        dta.RichContent = "文章内容详情页使用".decode("UTF-8")
        dta.DocContent = DocRes(Type=1, Url="www.**.com", PageNum=1)
        dta.Pictures = None
        dta.Videos = None

        tg = Tag()
        tg.TagId = 90003
        tg.TagName = "精选".decode("UTF-8")
        dta.Tags = [tg]
        dta.CreateTime = None
        dta.LastEditTime = None  # int(str(time.localtime())) * 1000
        dta.DisplayTextLink = "www.**.com"
        dta.OriginTextLink = "www.**.com"
        dta.State = 2
        dta.Origin = 1
        dta.LastTags = None
        dta.LastState = 2
        dta.RecommendTime = None    #int(str(time.localtime())) * 1000

        result = self.client.wc_new_article(dta)

        print result

    def test_wc_update_article(self):
        """更改文章, article也必须是全量内容"""
        dta = Article()

        user = User()
        user.Uid = 115775
        user.Nickname = "jwensh"

        # print chardet.detect("精选")

        dta.Id = 10006
        dta.Author = user
        dta.Type = 1
        dta.Title = "jwensh的后台thrift接口测试".decode("UTF-8")
        dta.SimpleContent = "jwensh文章内容列表页使用".decode("UTF-8")
        dta.RichContent = "jwensh文章内容详情页使用".decode("UTF-8")
        dta.DocContent = DocRes(Type=1, Url="www.**.com", PageNum=1)
        dta.Pictures = None
        dta.Videos = None

        tg = Tag()
        tg.TagId = 90003
        tg.TagName = "jwensh精选".decode("UTF-8")
        dta.Tags = [tg]
        dta.CreateTime = None
        dta.LastEditTime = int(time.time())
        dta.DisplayTextLink = "www.**.com"
        dta.OriginTextLink = "www.**.com"
        dta.State = 2
        dta.Origin = 1
        dta.LastTags = None
        dta.LastState = 2
        dta.RecommendTime = int(time.time())

        result = self.client.wc_update_article(dta)
        print result

    def test_wc_op_chang_state(self):
        """更改内容的状态"""
        dat = ChangeStateOp()
        dat.Id = 10001
        dat.Type = 1
        dat.State = 2

        result = self.client.wc_op_chang_state(dat)
        print result

    def test_wc_op_collect(self):
        """收藏/取消收藏操作"""
        dat = CollectOp()
        dat.Uid = 115775
        dat.Type = 2
        dat.Id = 10001
        dat.Timestamp = int(time.time())

        res = self.client.wc_op_collect(dat)
        print res