# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@software: PyCharm
@file: FinderType
@time: 2018/5/8  11:22
"""

from enum import Enum, unique

from selenium.webdriver.common.by import By


# @unique
class FindBy(By):
    pass
    # ID = By.ID
    # NAME = By.NAME
    # CLASS_NAME = By.CLASS_NAME
    # CSS_SELECTOR = By.CSS_SELECTOR
    # LINK_TEXT = By.LINK_TEXT
    # PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
    # TAG_NAME = By.TAG_NAME
    # XPATH = By.XPATH
