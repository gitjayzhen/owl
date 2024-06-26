# -*- encoding: utf-8 -*-

"""
@author: jayzhen 
@file: appium_controller.py
@time: 2024/3/26 23:08
"""

from owl.api.mobile.appium_driver import InitAppiumDriver
from owl.configs.appium_cfg import AppiumConfiger


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
        appium_props = AppiumConfiger()
        impl = InitAppiumDriver(appium_props)
        device_list = [self.sno]
        if self.sno is None:
            device_list = impl.android.get_device_list()
        work_api_list = {}
        if len(device_list) > 0:
            for d in device_list:
                work_api_list[d] = impl.get_appium_driver(d)
        return work_api_list

    def __str__(self):
        return "当前操作的设备号是 {} ".format(self.sno)
