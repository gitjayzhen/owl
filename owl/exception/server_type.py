# -*- coding: utf-8 -*-

"""
@author: jayzhen
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: server_type.py
@time: 2023/8/18 11:45
"""
from owl.exception import ExceptionMsg


class AppiumServiceNotRunningException(Exception):
    def __init__(self, message=ExceptionMsg.AppiumServiceNotRunning):
        self.message = message
        super().__init__(self.message)
