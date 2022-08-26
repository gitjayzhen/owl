#!/usr/bin/env python
# -*- coding:utf8 -*-

"""
这里主要管理接口固定的header，如果需要token、session、cookie等需要在进行添加
"""


class Header(object):

    def __init__(self):
        self.__pdl_header = {"Content-Type": "application/json",
                             "version": "1.0",
                             "filter-key": "filter-header",
                             "deviceType": "android",
                             "deviceModel": "MI 5s"}

        self.__lab_header = {"Host": "localhost:8080",
                             "Connection": "keep-alive",
                             "Content-Length": "20",
                             "Accept": "application/json, text/javascript, */*; q=0.01",
                             "Origin": "http://localhost:8080",
                             "X-Requested-With": "XMLHttpRequest",
                             "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                             "Referer": "http://localhost:8080/lab/classmanage",
                             "Accept-Encoding": "gzip, deflate, br",
                             "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"}

    def set_pdl_header(self, headers_to_add):
        """
            如果你想在基础的header上添加新的元素，可以直接传dict的格式过来
        """
        header = self.__pdl_header.copy()
        header.update(headers_to_add)
        self.__pdl_header = header

    def get_pdl_header(self):
        """返回header"""
        return self.__pdl_header

    def set_lab_header(self, headers_to_add):
        """
            如果你想在基础的header上添加新的元素，可以直接传dict的格式过来
        """
        header = self.__plab_header.copy()
        header.update(headers_to_add)
        self.__pdl_header = header

    def get_lab_header(self):
        """返回header"""
        return self.__lab_header

