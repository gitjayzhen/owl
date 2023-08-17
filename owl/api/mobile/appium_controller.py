# -*- encoding: utf-8 -*-

"""
@author: jayzhen 
@license: Apache Licence
@version: v1.0 
@contact: jayzhen_testing@163.com 
@site: https://blog.csdn.net/u013948858
@file: appium_controller.py
@time: 2017/12/26 23:08
"""
from owl.api.mobile.appium_api import AppiumBaseApi
from owl.api.mobile.appium_driver import InitAppiumDriver
from owl.configs.mobile_config import MobileConfigGetter


class PostRunController(object):
    """
    根据一个设备的sno号来确定一个 appium 操作手
    需要做的是单机模式和多机模式
    """

    def __init__(self, sno=None):
        """
        @param sno{string} : 可以指定 sno ,也可以不指定，不指定就用连接的设备中的一个
        """
        self.sno = sno

    def get_device_map_appium(self):
        props = MobileConfigGetter()
        impl = InitAppiumDriver(props.properties)
        device_list = [self.sno]
        if self.sno is None:
            device_list = impl.android.get_device_list()
        api_list = {}
        if len(device_list) > 0:
            for d in device_list:
                driver = impl.get_android_driver(d)
                api = AppiumBaseApi(driver)
                api_list[d] = api
        return api_list

    def __str__(self):
        return "当前是设备{}的操作者".format("testing")
