# -*- encoding: utf-8 -*-

"""
@author: jayzhen 
@license: Apache Licence
@version: v1.0 
@contact: jayzhen_testing@163.com 
@site: https://blog.csdn.net/u013948858
@file: controller.py
@time: 2017/12/26 23:08
"""
from owl.api.mobile.appium_api import AppiumBaseApi
from owl.api.mobile.appium_driver import InitAppiumDriver


class MobileController(object):
    """
    根据一个设备的sno号来确定一个 appium 操作手
    需要做的是单机模式和多机模式
    """

    def __init__(self):
        self.impl = InitAppiumDriver()
        self.dl = self.impl.android.get_device_list()

    def get_ctl_list(self):
        api_list = []
        if self.dl is not None and len(self.dl) >= 1:
            for i in range(len(self.dl)):
                driver = self.impl.get_android_driver(self.dl[i])
                api = AppiumBaseApi(driver)
                api_list.append(api)

    def __str__(self):
        return "当前是设备{}的操作者".format("testing")
