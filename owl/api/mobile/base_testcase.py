# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@file: base_testcase.py
@time: 2024/3/25 13:24
"""
import random

from owl.api.mobile.appium_api import AppiumWorkApi
from owl.api.mobile.appium_controller import PostRunController


class BaseTestCase:
    """
    测试用例可以继承，以达到节省代码
    """
    driver = None

    def setup(self):
        # 根据当前链接的设备，实例化 appium server
        devices = PostRunController().get_device_map_appium()
        assert len(devices.keys()) > 0, "No device connection"
        self.driver: AppiumWorkApi = devices.get(random.choice(list(devices.keys())))

    def teardown(self):
        if self.driver.driver:
            self.driver.driver.quit()
