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

    @pytest.mark.parametrize("driver", WebDriverDoBeforeTest().get_api_driver())
    def test_local_webdriver_run(self, driver):
        driver.get("http://baidu.com")


if __name__ == '__main__':
    TestSeleniumInLocal().test_local_webdriver_run()