# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: test_http_one.py
@time: 2023/8/16 12:43
"""
import json

import requests

from owl.api.interface.http_requests import Requester


class TestHttpInterface:

    def test_http_interface(self):
        """
        3A 原则
        """
        url = "https://api.vvhan.com/api/hotlist?type=baiduRD"
        resp = Requester().do_get(url=url)
        assert resp['success'], "接口请求异常"
