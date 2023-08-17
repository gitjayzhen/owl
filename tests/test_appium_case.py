# -*- coding: utf-8 -*-

"""
@author: jayzhen <jayzhen_testing@163.com>
@site: https://github.com/gitjayzhen
@version: 1.0.0
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: test_appium_case.py
@time: 2023/8/17 14:10
"""

# emulator -avd Nexus_5X_API_23 -netdelay none -netspeed full

import unittest
import random

from appium.webdriver.common.mobileby import MobileBy

from owl.api.mobile.appium_controller import PostRunController
from owl.api.mobile.appium_driver import InitAppiumDriver
from owl.api.mobile.appium_api import AppiumBaseApi
from owl.configs.mobile_config import MobileConfigGetter


class TestAppiumBaseApi(unittest.TestCase):

    def setUp(self):
        devices = PostRunController().get_device_map_appium()
        print(devices)
        self.driver: AppiumBaseApi = devices.get(random.choice(list(devices.keys())))

    def tearDown(self):
        self.driver.driver.quit()

    # @unittest.skip("skip 'test_is_displayed' func")
    def test_is_displayed(self):
        print(self.driver.is_displayed(MobileBy.ID, "com.youku.phone:id/img_user"))

    @unittest.skip("skip 'test_find_element_by_want' func")
    def test_find_element_by_want(self):
        print(self.driver.find_element_by_want(MobileBy.ID, "com.youku.phone:id/img_user", 5))

    def test_get_current_activity(self):
        print(self.driver.get_current_activity())


if __name__ == '__main__':
    unittest.main()
