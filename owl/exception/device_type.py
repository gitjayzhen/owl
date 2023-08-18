# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: device_type.py
@time: 2023/8/18 16:37
"""
from owl.exception import ExceptionMsg


class NoDeviceConnectionException(Exception):
    def __init__(self, message=ExceptionMsg.NoDeviceConnection):
        self.message = message
        super().__init__(self.message)
