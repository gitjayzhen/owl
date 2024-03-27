#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jayzhen
@file: test_ui_se_local.py
@time: 2023/3/25 12:49
"""
from owl.api.browser.base_testcase import BaseTestCase
from owl.domain.selector_enum import FindBy


class TestSeleniumInLocal(BaseTestCase):

    def test_local_webdriver_run(self):
        self.driver.get("https://baidu.com")
        self.driver.send_keys(FindBy.CSS_SELECTOR, "#kw", "jayzhen")
        self.driver.click(FindBy.CSS_SELECTOR, "#su")
        self.driver.capture()
