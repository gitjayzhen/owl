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
from enum import Enum, unique, EnumMeta


class EnumDirectValueMeta(EnumMeta):
    """
    可以解决调用枚举属性时，由类型 enum 变成 string
    需要枚举类继承: Enum, metaclass=EnumDirectValueMeta
    """
    def __getattribute__(cls, name):
        value = super().__getattribute__(name)
        if isinstance(value, cls):
            value = value.value
        return value


@unique
class ExceptionMsg(Enum, metaclass=EnumDirectValueMeta):

    AppiumServiceNotRunning = "the appium service is not running"
    NoDeviceConnection = "no mobile devices are connected to the current machine"
    SingletonInstantiation = "This class is a singleton!"
