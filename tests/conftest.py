# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: conftest.py
@time: 2024/4/8 11:33
"""

import pytest


@pytest.fixture(scope='session', autouse=True)
def init_data():
    """
    初始化，获取session
    :return:
    """
    print(f'test init data')


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的 item 的 name 和 nodeid 的中文显示在控制台上，防止 pytest-html 报告中文乱码
    """
    for item in items:
        item.name = item.name
        item._nodeid = item.nodeid