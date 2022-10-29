#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author: jayzhen
@email: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm & Python 2.7
@file: request_builder.py
@time: 2018/06/26 19:13 
"""
import re
import pandas as pd

from framework.utils.fileUtil.FileInspector import FileInspector
from framework.domain.request_struct import DataStruct
from framework.api.interface.http_requests import Requester
from styleframe import Styler, utils, StyleFrame


class RequestBuilder(object):

    def __init__(self):
        fc = FileInspector()
        self.filepath = None
        self.propath = None
        boolean = fc.is_has_file("接口测试用例集.xlsx")
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
