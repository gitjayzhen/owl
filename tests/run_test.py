# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: run_test.py
@time: 2024/4/8 11:32
"""

import os
import shutil
import pytest

config = object()


def run_cases():
    # if os.path.exists(config.log_path):
    #     shutil.rmtree(config.log_path)
    #
    # if os.path.exists(config.report_path):
    #     shutil.rmtree(config.report_path)

    pytest.main(['./test_http_one.py', './owl/test_file_inspector.py', '-sv', '--reruns=2', '--alluredir=logs/report', '--clean-alluredir'])
    os.system('allure generate logs/report -o logs/html --clean')
    os.system('allure serve logs/report')


if __name__ == '__main__':
    run_cases()
