# -*- coding:UTF-8 -*-
"""
Created on 2016年4月26日
@author: jayzhen
"""

import os

from com.framework.utils.fileUtil.ConfigReader import ConfigReader
from com.framework.utils.fileUtil.FileInspector import FileInspector
from com.framework.utils.reporterUtil.LoggingPorter import LoggingPorter
from com.framework.web.domain.SeIniDomain import SeIniDomain

"""
读取配置文件.conf的内容，返回driver的绝对路径
"""


class WebConfingGetter(object):
    def __init__(self):
        self.__fileabspath = None
        self.__projectpath = None
        self.log4py = LoggingPorter()
        fc = FileInspector()
        boolean = fc.is_has_file("owl-selenium.ini")
        if boolean: 
            self.__fileabspath = fc.get_file_abspath()
            self.__projectpath = fc.get_project_path()
        self.conf = ConfigReader(self.__fileabspath)

    @property
    def properties(self):
        """
        获取配置文件中的内容并返回对应的对象
        :return:
        """
        wp = SeIniDomain()
        try:
            wp.pageLoadTimeout = self.conf.get_value("TimeSet", "pageLoadTimeout")
            wp.waitTimeout = self.conf.get_value("TimeSet", "waitTimeout")
            wp.scriptTimeout = self.conf.get_value("TimeSet", "scriptTimeout")
            wp.pauseTime = self.conf.get_value("TimeSet", "pauseTime")

            wp.capturePath = os.path.join(self.__projectpath, self.conf.get_value("ResultPath", "capturePath"))
            if not os.path.exists(wp.capturePath):
                os.makedirs(wp.capturePath)
            wp.htmlreportPath = os.path.join(self.__projectpath, self.conf.get_value("ResultPath", "htmlreportPath"))
            if not os.path.exists(wp.htmlreportPath):
                os.makedirs(wp.htmlreportPath)
            wp.logsPath = os.path.join(self.__projectpath, self.conf.get_value("ResultPath", "logsPath"))
            if not os.path.exists(wp.logsPath):
                os.makedirs(wp.logsPath)
            wp.baseURL = self.conf.get_value("baseURL", "baseURL")
            wp.browser = self.conf.get_value("run", "browser")
            wp.type = self.conf.get_value("run", "type")
            wp.browserdriver = os.path.join(self.__projectpath, self.conf.get_value("driver", wp.browser))

            if wp.type == "0":
                d = {}
                d['url'] = self.conf.get_value('remoteProfile', 'url')
                d['browserName'] = self.conf.get_value('remoteProfile', 'browserName')
                d['version'] = self.conf.get_value('remoteProfile', 'version')
                d['maxinstance'] = self.conf.get_value('remoteProfile', 'maxinstance')
                d['platform'] = self.conf.get_value('remoteProfile', 'platform')
                wp.remoteProfile = d
        except Exception, e:
            self.log4py.error("实例化selenium配置文件对象时，出现异常 ：" + str(e))
        return wp
