# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@file: base_testcase.py
@time: 2024/3/25 13:24
"""

from owl.api.browser.selenium_driver import BrowserDriver


class BaseTestCase:
    """
    测试用例可以继承，以达到节省代码
    """
    driver = None

    # 方法级开始--类里每个测试方法执行前执行
    def setup(self):
        self.driver = BrowserDriver(self).init_driver()
        assert self.driver, "init driver error, recheck"

    # 方法级结束--类里每个测试方法执行后执行
    def teardown(self):
        if self.driver:
            self.driver.stop_web_driver()
