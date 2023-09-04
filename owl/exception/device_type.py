# -*- coding: utf-8 -*-

"""
@author: jayzhen
@file: device_type.py
@time: 2023/8/18 16:37
"""
from owl.exception import ExceptionMsg


class NoDeviceConnectionException(Exception):
    def __init__(self, message=ExceptionMsg.NoDeviceConnection):
        self.message = message
        super().__init__(self.message)
