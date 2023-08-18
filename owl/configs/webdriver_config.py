# -*- coding:UTF-8 -*-

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
        boolean = fc.is_has_file("owl-selenium.ini")
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
            wp.pageLoadTimeout = self.conf.get_value("TimeSet", "pageLoadTimeout")
            wp.waitTimeout = self.conf.get_value("TimeSet", "waitTimeout")
            wp.scriptTimeout = self.conf.get_value("TimeSet", "scriptTimeout")
            wp.pauseTime = self.conf.get_value("TimeSet", "pauseTime")

            wp.capturePath = os.path.join(self.__project_path, self.conf.get_value("ResultPath", "capturePath"))
            if not os.path.exists(wp.capturePath):
                os.makedirs(wp.capturePath)
            wp.htmlreportPath = os.path.join(self.__project_path, self.conf.get_value("ResultPath", "htmlreportPath"))
            if not os.path.exists(wp.htmlreportPath):
                os.makedirs(wp.htmlreportPath)
            wp.logsPath = os.path.join(self.__project_path, self.conf.get_value("ResultPath", "logsPath"))
            if not os.path.exists(wp.logsPath):
                os.makedirs(wp.logsPath)
            wp.baseURL = self.conf.get_value("baseURL", "baseURL")
            wp.browser = self.conf.get_value("run", "browser")
            wp.type = self.conf.get_value("run", "type")
            wp.browserdriver = os.path.join(self.__project_path, self.conf.get_value("driver", wp.browser))
            wp.isHeadless = self.conf.get_value("driver", "isHeadless")
            print(wp.browserdriver)
            if wp.type == "0":
                d = {'url': self.conf.get_value('remoteProfile', 'url'),
                     'browserName': self.conf.get_value('remoteProfile', 'browserName'),
                     'browserVersion': self.conf.get_value('remoteProfile', 'browserVersion'),
                     'maxinstance': self.conf.get_value('remoteProfile', 'maxInstance'),
                     'platformName': self.conf.get_value('remoteProfile', 'platformName')}
                wp.remoteProfile = d
        except Exception as e:
            self.log4py.error("实例化selenium配置文件对象时，出现异常 ：" + str(e))
        return wp
