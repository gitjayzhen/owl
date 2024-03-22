# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: webdriver_cfg.py
@time: 2023/9/5 10:39
"""


import os

from owl.domain.se_config_do import SeleniumIniDomain
from owl.lib.file.config_resolver import ConfigControl
from owl.lib.file.file_inspector import FileInspector
from owl.lib.reporter.logging_porter import LoggingPorter


class WebdriverConfiger(object):
    """
    读取配置文件.conf的内容，返回driver的绝对路径
    """

    def __init__(self):
        self.__file_abs_path = None
        self.__project_path = None
        self.log4py = LoggingPorter()
        fc = FileInspector()
        boolean = fc.is_has_file("owl.ini")
        if boolean:
            self.__file_abs_path = fc.get_file_abspath()
            self.__project_path = fc.get_project_path()
        self.conf = ConfigControl(self.__file_abs_path)

    @property
    def properties(self):
        """
        获取配置文件中的内容并返回对应的对象
        :return:
        """
        wp = SeleniumIniDomain()
        try:
            wp.pageLoadTimeout = self.conf.get_value("selenium.TimeSet", "pageLoadTimeout")
            wp.waitTimeout = self.conf.get_value("selenium.TimeSet", "waitTimeout")
            wp.scriptTimeout = self.conf.get_value("selenium.TimeSet", "scriptTimeout")
            wp.pauseTime = self.conf.get_value("selenium.TimeSet", "pauseTime")

            wp.capturePath = os.path.join(self.__project_path, self.conf.get_value("selenium.ResultPath", "capturePath"))
            if not os.path.exists(wp.capturePath):
                os.makedirs(wp.capturePath)
            wp.htmlreportPath = os.path.join(self.__project_path, self.conf.get_value("selenium.ResultPath", "htmlreportPath"))
            if not os.path.exists(wp.htmlreportPath):
                os.makedirs(wp.htmlreportPath)
            wp.logsPath = os.path.join(self.__project_path, self.conf.get_value("selenium.ResultPath", "logsPath"))
            if not os.path.exists(wp.logsPath):
                os.makedirs(wp.logsPath)
            wp.baseURL = self.conf.get_value("selenium.baseURL", "baseURL")
            wp.browser = self.conf.get_value("selenium.run", "browser")
            wp.type = self.conf.get_value("selenium.run", "type")
            wp.browserdriver = self.get_file_path(
                os.path.join(self.__project_path,
                             self.conf.get_value("selenium.driver", wp.browser)
                             ), "SELENIUM_DRIVER")
            wp.isHeadless = self.conf.get_value("selenium.driver", "isHeadless")
            print(wp.browserdriver)
            if wp.type == "0":
                d = {'url': self.conf.get_value('selenium.remoteProfile', 'url'),
                     'browserName': self.conf.get_value('selenium.remoteProfile', 'browserName'),
                     'browserVersion': self.conf.get_value('selenium.remoteProfile', 'browserVersion'),
                     'maxinstance': self.conf.get_value('selenium.remoteProfile', 'maxInstance'),
                     'platformName': self.conf.get_value('selenium.remoteProfile', 'platformName')}
                wp.remoteProfile = d
        except Exception as e:
            self.log4py.error("实例化selenium配置文件对象时，出现异常 ：" + str(e))
        return wp

    def get_file_path(self, prop_path, env_key):
        if not self.is_absolute_and_exists(prop_path):
            return os.environ.get(env_key)
        return prop_path

    @classmethod
    def is_absolute_and_exists(cls, path):
        if os.path.isabs(path) and os.path.exists(path):
            return True
        return False
