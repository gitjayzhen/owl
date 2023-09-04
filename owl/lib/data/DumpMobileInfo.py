# -*- encoding: utf-8  -*-

""" 
@author: jayzhen
@time: 2017/7/27 23:29
"""

import json
import os
import wx
from owl.lib.file.file_inspector import FileInspector
"""
这个类中主要用于将手机的基础信息以json的形式保存到文档中
"""


class DumpMobileInfo(object):
    def __init__(self):
        self.json_obj = None
        self.fp = FileInspector()
        self.json_file_path = self.fp.get_devices_info_file_path()

    def load_json(self, json_file_path):
        fin = open(json_file_path, "r")
        try:
            self.json_obj = json.load(fin)
        except ValueError as e:
            self.json_obj = {}
        fin.close()
        return self.json_obj

    def get_value_with_key(self, json_key):
        return self.json_obj[json_key]

    def put_key_value(self, dict_data):
        try:
            json_obj = self.load_json(self.json_file_path)
            n = 0
            for k in dict_data:
                # if not json_obj.has_key(k):
                if k not in json_obj:
                    json_obj[k] = dict_data[k]
                    n += 1
            if n == 0:
                wx.LogMessage("this phone info has done")
                return None
            with open(self.json_file_path, 'w+') as json_f_obj:
                json_f_obj.write(json.dumps(json_obj, sort_keys=True, indent=4, separators=(',', ': '),encoding="gbk",ensure_ascii=True))
        except Exception as e:
            wx.LogMessage(str(e))
        else:
            wx.LogMessage("device info collect work has done, go to check json file")
