# -*- coding: utf-8 -*-

"""
@author: jayzhen
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: __init__.py
@time: 2023/8/18 11:44
"""
from enum import Enum, unique

from owl.lib.common import EnumDirectValueMeta


@unique
class ExceptionMsg(Enum, metaclass=EnumDirectValueMeta):

    AppiumServiceNotRunning = "the appium service is not running"
    NoDeviceConnection = "no mobile devices are connected to the current machine"
    SingletonInstantiation = "This class is a singleton!"
    BrowserDriverError = "The browser failed to instantiate the driver, please recheck"
