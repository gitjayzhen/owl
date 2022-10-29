#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@email: jayzhen_testing@163.com
@software: PyCharm
@file: requester.py
@time: 2017/9/4 23:25

单下划线、双下划线、头尾双下划线说明：
__foo__: 定义的是特列方法，类似 __init__() 之类的。
_foo: 以单下划线开头的表示的是保护protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
__foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

也就是说class的变量自己可以访问，实例化的对象可以访问，类内部（其实可是实例化对象后）可以访问
对象变量类不能访问，对象可以访问，但是对象属性在__init__中初始化不一定有类型，可以通过私有类对象类解决（http://www.cnblogs.com/wxfasdic/archive/2012/07/10/2583887.html）
设计：使用私有类型变量，赋予类型，在__init__中行进行初始化，或者get/set操作

类属性与方法
类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods
"""


class RequestData(object):

    # 类变量，可以直接用类名调用，也可以用对象调用
    class_var = "qerqeerqwerwerqw"
    # 私有变量
    __private_var = "124324"

    def __init__(self):
        self.method = None
        self.url = None
        self.params = None
        self.data = None
        self.headers = None
        self.cookies = None
        self.timeout = None
        self.verify = None
        self.cert = None
        self.json = None

    def get_method(self):
        return self.method

    def set_method(self, method):
        self.method = method

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.method = data

    def get_headers(self):
        return self.headers

    def set_headers(self, headers):
        self.headers = headers

    def get_cookies(self):
        return self.cookies

    def set_cookies(self, cookies):
        self.cookies = cookies

    def get_timeout(self):
        return self.timeout

    def set_timeout(self, timeout):
        self.timeout = timeout

    def get_verify(self):
        return self.verify

    def set_verify(self, verify):
        self.verify = verify

    def get_cert(self):
        return self.cert

    def set_cert(self, cert):
        self.cert = cert

    def get_json(self):
        return self.json

    def set_json(self, json):
        self.json = json

    def to_string(self):
        print(self.class_var)
        print(self.__private_var)
        return "RequestData [method:"+str(self.method)+", url:"+str(self.url) + \
               ", params:"+str(self.params)+", data:"+str(self.data) + \
               ", headers:"+str(self.headers)+", cookies:"+str(self.cookies) + \
               ", timeout"+str(self.timeout)+", verify:"+str(self.verify) + \
               ", cert:"+str(self.cert)+", json:"+str(self.json) + "]"
