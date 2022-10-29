# -*- coding:utf8 -*-

import os
import json
from requests import Session, Request
from framework.utils.reporter_util.logging_porter import LoggingPorter

"""
作为核心的请求发送model，需要处理请求的header和body及发送
"""


class Requester(object):

    def __init__(self):
        self.log4py = LoggingPorter()
        self.timeout = 5
        self.s = Session()

    def init_config(self, url, headers, data):
        """
        主要这个处理header的构建和接口超时或重试设置
        :return:
        """
        flag = True
        if url is None or url == "":
            raise ValueError(" url cant be empty ! ")
        if headers is None or headers == "":
            self.log4py.debug("post 请求的header为空")
        if data is None or data == "":
            self.log4py.debug("post 请求的data为空")
        return flag

    def POST_FORM(self, url, headers, form_data):
        """
        url必须入参、headers可选入参、form_data可选入参
        这个方法处理的是将表单中的数据提交数据库，就是‘x-www-form-urlencoded’的内容
        """
        if self.init_config(url, headers, form_data):
            result = self.execute_request('POST', url, req_headers=headers, req_data=form_data)
            return result
        return None

    def POST_JSON(self, url, headers, json_data):
        """
        url必须入参、headers可选入参、json可选入参(data和json看后台接口需要识别什么形式的)
        接口如果使用json传输数据 ，那就使用这个也就是‘Content-Type: Application/json’
        """
        if self.init_config(url, headers, json_data):
            post_response = self.execute_request('POST', url, req_headers=headers, req_json=json_data)
            return post_response
        return None

    def POST(self, url, headers, form_data, json_data):
        """
        如果一个接口又是json又有form，就是用这个方法，但是我没有见过，姑且写上
        """
        if json_data is None or json_data == "":
            self.log4py.debug("post 请求的json data为空")
        if self.init_config(url, headers, form_data):
            result = self.execute_request('POST', url, req_headers=headers, req_data=form_data, req_json=json_data)
            return result
        return None

    def do_get(self, url, req_headers, req_params):
        """
        url必须入参、headers可选入参、params可选入参
        """
        if url is None or url == "":
            self.log4py.debug("get请求的url为空".decode("utf-8"))
            return None
        if req_headers is None or req_headers == "":
            self.log4py.debug("get请求的header为空".decode("utf-8"))
            req_headers = None
        if req_params is None or req_params == "":
            self.log4py.debug("get请求的parameter为空".decode("utf8"))
            req_params = None
        self.execute_request(method="get", url=url, req_headers=req_headers, req_params=req_params)

    def do_put(self, url, data, file_name):
        work_path = os.getcwd()
        f = open(os.path.join(work_path, file_name))
        json_data = json.dumps(f.read())
        f.close()
        s = Session()
        req = Request('PUT', url, json=json_data, headers=self.headers)
        prepped = req.prepare()
        resp = s.send(prepped, verify=True)
        s.close()
        if resp.ok:
            return True
        return False

    def execute_request(self, method, url, **key_value):
        """
         request(method, url, params=None, data=None, headers=None, cookies=None, timeout=None, verify=None, cert=None, json=None)
        :param method:
        :param url:
        :param key_value:
        :return:
        """
        req_params = None
        req_json = None
        req_headers = None
        req_data = None
        for key in key_value:
            if "req_params" == key:
                req_params = key_value[key]
            elif "req_json" == key:
                req_json = key_value[key]
            elif "req_headers" == key:
                req_headers = key_value[key]
            elif "req_data" == key:
                req_data = key_value[key]
        self.log4py.debug("{}接口{}请求的参数：header：{}; params: {}; data: {}; json: {}".format(url, method, req_headers, req_params, req_data, req_json))
        # s = Session()
        req = Request(method, url, params=req_params, data=req_data, headers=req_headers, json=req_json)
        # prepped = req.prepare()
        prepped = self.s.prepare_request(req)  # 建议使用这种方法
        resp = self.s.send(prepped, verify=True, timeout=self.timeout)

        # self.log4py.debug("返回结果：{} - {}".format(resp.status_code, resp.text.encode("utf-8")))
        try:
            res_json = resp.json()
            return res_json
        except ValueError as ve:
            self.log4py.debug("解析json返回结果出错：{}".format(ve))
        self.s.close()
        return resp


