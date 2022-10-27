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
from framework.driver.web_driver_base import WebDriverDoBeforeTest


class TestSeleniumInLocal(WebDriverDoBeforeTest):
    
    def __init__(self):
        super(TestSeleniumInLocal, self).__init__(self)

    def test_local_webdriver_run(self):
        se_driver = self.get_api_driver()
        se_driver.get("http://baidu.com")


if __name__ == '__main__':
    TestSeleniumInLocal().test_local_webdriver_run()