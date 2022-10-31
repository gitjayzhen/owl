#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jay.zhen
@contact: jayzhen_testing@163.com
@version: 1.0.0
@license: Apache Licence
@file: test_se_local.py
@time: 2022/10/27 18:49
"""
import pytest
from framework.driver.se_web_driver import WebDriverDoBeforeTest


class TestSeleniumInLocal:

    driver = None

    # 方法级开始--类里每个测试方法执行前执行
    def setup(self):
        print("-->setup_method1")

    # 方法级结束--类里每个测试方法执行后执行
    def teardown(self):
        print("-->teardown_method1")

    @pytest.mark.parametrize("driver", WebDriverDoBeforeTest().get_api_driver())
    def test_local_webdriver_run(self, driver):
        driver.get("http://baidu.com")


if __name__ == '__main__':
    TestSeleniumInLocal().test_local_webdriver_run()