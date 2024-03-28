# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: owl_type.py
@time: 2023/9/4 17:11
"""
from owl.exception import ExceptionMsg


class SingletonInstantiationException(Exception):
    def __init__(self, message=ExceptionMsg.SingletonInstantiation):
        self.message = message
        super().__init__(self.message)


class BrowserDriverError(Exception):
    def __init__(self, message=ExceptionMsg.BrowserDriverError):
        self.message = message
        super().__init__(self.message)
