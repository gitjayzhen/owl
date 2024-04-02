# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: selenium_cfg.py
@time: 2023/9/5 10:39
"""


import os

from owl.configs import BaseOwlConfiger
from owl.domain.se_config_do import SeleniumIniDomain


class SeleniumConfiger(BaseOwlConfiger):
    """
    读取配置文件.conf的内容，返回driver的绝对路径
    """

    def __init__(self):
        super().__init__()

    @property
    def properties(self):
        """
        获取配置文件中的内容并返回对应的对象
        :return:
        """
        wp = SeleniumIniDomain()
        try:
            wp.pageLoadTimeout = self.cfg.get_value("selenium.driver", "pageLoadTimeout")
            wp.waitTimeout = self.cfg.get_value("selenium.driver", "waitTimeout")
            wp.scriptTimeout = self.cfg.get_value("selenium.driver", "scriptTimeout")
            wp.pauseTime = self.cfg.get_value("selenium.driver", "pauseTime")

            wp.capturePath = os.path.join(self.__project_root_path, self.cfg.get_value("selenium.run", "capturePath"))
            if not os.path.exists(wp.capturePath):
                os.makedirs(wp.capturePath)
            wp.htmlReportPath = os.path.join(self.__project_root_path, self.cfg.get_value("selenium.run", "htmlReportPath"))
            if not os.path.exists(wp.htmlReportPath):
                os.makedirs(wp.htmlReportPath)
            wp.browser = self.cfg.get_value("selenium.run", "browser")
            wp.type = self.cfg.get_value("selenium.run", "type")
            wp.browserDriver = self.get_file_path(
                os.path.join(self.__project_root_path,
                             self.cfg.get_value("selenium.driver", wp.browser)
                             ), "SELENIUM_DRIVER")
            wp.isHeadless = self.cfg.get_value("selenium.driver", "isHeadless")
            print(wp.browserDriver)
            if wp.type == "0":
                d = {'url': self.cfg.get_value('selenium.run', 'nodeURL'),
                     'browserName': self.cfg.get_value('selenium.run', 'browserName'),
                     'browserVersion': self.cfg.get_value('selenium.run', 'browserVersion'),
                     'maxinstance': self.cfg.get_value('selenium.run', 'maxInstance'),
                     'platformName': self.cfg.get_value('selenium.run', 'platformName')}
                wp.remoteProfile = d
        except Exception as e:
            self.log4py.error("实例化selenium配置文件对象时，出现异常 ：" + str(e))
        return wp

