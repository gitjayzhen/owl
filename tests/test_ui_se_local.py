#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jay.zhen
@version: 1.0.0
@license: Apache Licence
@file: test_ui_se_local.py
@time: 2022/10/27 18:49
"""

from owl.api.browser.selenium_driver import BrowserDriver
from owl.domain.selector_enum import FindBy


class TestSeleniumInLocal:

    driver = None

    # 方法级开始--类里每个测试方法执行前执行
    def setup(self):
        self.driver = BrowserDriver(self).get_driver()

    # 方法级结束--类里每个测试方法执行后执行
    def teardown(self):
        self.driver.stop_web_driver()

    def test_local_webdriver_run(self):
        self.driver.get("https://baidu.com")
        self.driver.send_keys(FindBy.CSS_SELECTOR, "#kw", "jayzhen")
        self.driver.click(FindBy.CSS_SELECTOR, "#su")
        self.driver.capture()
