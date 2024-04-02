# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license:  Apache Licence
@software: PyCharm & Python 3.7+
@file: test_appium_case.py
@time: 2023/8/17 14:10
"""
import pytest
from appium.webdriver.common.mobileby import MobileBy

from owl.api.mobile.base_testcase import BaseTestCase


class TestAppiumBaseApi(BaseTestCase):
    """
    emulator -avd Nexus_5X_API_23 -netdelay none -netspeed full
    """

    # @pytest.mark.skip("skip 'test_is_displayed' func")
    def test_is_displayed(self):
        print(self.driver.is_displayed(MobileBy.ID, "com.youku.phone:id/img_user"))

    @pytest.mark.skip("skip 'test_find_element_by_want' func")
    def test_find_element_by_want(self):
        print(self.driver.find_element_by_want(MobileBy.ID, "com.youku.phone:id/img_user", 5))

    def test_get_current_activity(self):
        print(self.driver.get_current_activity())
