# -*- coding:utf8 -*-

import json
import os
import re

import pandas as pd
from requests import Session, Request
from styleframe import Styler, utils, StyleFrame

from owl.domain.request_struct_do import DataStruct
from owl.lib.file.file_inspector import FileInspector
from owl.lib.reporter.logging_porter import LoggingPorter


class Requester(object):
    """
    作为核心的请求发送 model，需要处理请求的header和body及发送
    """

    def __init__(self):
        self.log4py = LoggingPorter()
        self.timeout = 5
        self.s = Session()
        self.headers = None

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

    def post_form(self, url, headers=None, form_data=None):
        """
        url必须入参、headers可选入参、form_data可选入参
        这个方法处理的是将表单中的数据提交数据库，就是‘x-www-form-urlencoded’的内容
        """
        if self.init_config(url, headers, form_data):
            result = self.execute_request('POST', url, req_headers=headers, req_data=form_data)
            return result
        return None

    def post_json(self, url, headers=None, json_data=None):
        """
        url必须入参、headers可选入参、json可选入参(data和json看后台接口需要识别什么形式的)
        接口如果使用json传输数据 ，那就使用这个也就是‘Content-Type: Application/json’
        """
        if self.init_config(url, headers, json_data):
            post_response = self.execute_request('POST', url, req_headers=headers, req_json=json_data)
            return post_response
        return None

    def post(self, url, headers, form_data, json_data):
        """
        如果一个接口又是json又有form，就是用这个方法，但是我没有见过，姑且写上
        """
        if json_data is None or json_data == "":
            self.log4py.debug("post 请求的json data为空")
        if self.init_config(url, headers, form_data):
            result = self.execute_request('POST', url, req_headers=headers, req_data=form_data, req_json=json_data)
            return result
        return None

    def do_get(self, url, req_headers=None, req_params=None):
        """
        url必须入参、headers可选入参、params可选入参
        """
        if url is None or url == "":
            self.log4py.debug("get请求的url为空")
            return None
        if req_headers is None or req_headers == "":
            self.log4py.debug("get请求的header为空")
            req_headers = None
        if req_params is None or req_params == "":
            self.log4py.debug("get请求的parameter为空")
            req_params = None
        return self.execute_request(method="get", url=url, req_headers=req_headers, req_params=req_params)

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


class RequestBuilder(object):

    def __init__(self):
        fc = FileInspector()
        self.filepath = None
        self.propath = None
        boolean = fc.is_has_file("interface-test-case.xlsx")
        if boolean:
            self.filepath = fc.get_file_abspath()
            self.propath = fc.get_project_path()

    def data_mapping(self, source, obj):
        """
        将excel读取的行数据，映射成一个操作对象，共测试报告使用
        :param source: 读取的excel row
        :param obj: domain数据对象
        :return: obj
        """
        if source is None:
            return None
        if isinstance(source, tuple) and isinstance(obj, DataStruct):
            obj_attr = dir(obj)
            for i in obj_attr:
                if i.startswith("__"):
                    continue
                obj.__setattr__(i, source.__getattribute__(i))
        return obj

    def send_req(self, ds):
        """
        将excel中的接口数据发送出去
        :param ds: domain对象
        :return: None
        """
        if ds is None:
            return None
        req = Requester()
        resp = req.execute_request(ds.method, ds.url)
        if re.findall(ds.assertion, resp.text):
            ds.result = resp.status_code
            ds.notes = str(resp.headers)

    def get_sheet_table(self):
        """
        需要处理的时将excel的内容读出来和修改内容并保存
        :return:
        """
        # 读取一个excel的文本文件（当前默认时读一个文件的一个sheet页）
        ex = pd.read_excel(self.filepath.encode('utf-8').decode("unicode_escape"))
        # 用pd格式化
        df = pd.DataFrame(ex)
        # 迭代器遍历sheet页里的内容
        for row in df.itertuples(name="RowData"):
            # 实例化一个数据模型对象
            ds = DataStruct()
            # 用读到的excel行数据来填充这个对象
            self.data_mapping(row, ds)
            # 通过这个对象的属性值，来发起一次request请求，在请求的过程把结果及校验的数据处理完后，
            self.send_req(ds)
            print(ds.__dict__)
            # 接口发起后的结果写入到excel对应行的对应列中
            # 执行修改操作
            df.update(pd.Series(ds.result, name="test_result", index=[row.Index]))
            df.update(pd.Series(ds.notes, name="test_notes", index=[row.Index]))

        # 执行数据更新后的保存操作：这里有个问题就是源文件覆盖保存，会没有特定的样式，需要再升级一下
        # df.to_excel(unicode(self.filepath, "utf8"))

        # 创建StyleFrame对象，该对象包装我们的DataFrame并分配默认样式。
        defaults = {'font': utils.fonts.aharoni, 'font_size': 12}
        sf = StyleFrame(df, styler_obj=Styler(**defaults))

        """
        # Style the headers of the table
        header_style = Styler(bold=True, font_size=14)
        sf.apply_headers_style(styler_obj=header_style)

        # Change the columns width and the rows height
        sf.set_column_width(columns=sf.columns, width=20)
        sf.set_row_height(rows=sf.row_indexes, height=90)
        """

        sf.set_column_width_dict(col_width_dict={
            ('cid', 'type', 'method', 'result'): 7,
            ('project', 'module', 'function', 'desc', 'protocol', 'assertion'): 13,
            ('url',): 20,
            ('header', 'cookie', 'entity', 'assertion', 'notes'): 30
        })
        row_num = sf.row_indexes
        sf.set_row_height_dict(row_height_dict={
            row_num[0]: 28,
            row_num[1:]: 90
        })

        sf.apply_headers_style(styler_obj=Styler(bg_color=utils.colors.grey))

        sf.to_excel(self.filepath.encode('utf-8').decode("unicode_escape")).save()
        print(30 * "*")


if __name__ == "__main__":
    rb = RequestBuilder()
    rb.get_sheet_table()

