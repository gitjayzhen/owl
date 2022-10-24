# -*- coding:UTF-8 -*-
"""
Created on 2016年4月26日
@author: jayzhen
"""

import os
from framework.utils.fileUtil.ConfigReader import ConfigReader
from framework.utils.fileUtil.FileInspector import FileInspector
from framework.mobile.domain.AppiumIniDomain import AppiumIniDomain
from framework.utils.reporter_util.logging_porter import LoggingPorter

"""
读取配置文件.conf的内容，返回driver的绝对路径
"""


class MobileConfigGetter(object):
    def __init__(self):
        self.__fileabspath = None
        self.__projectpath = None
        self.log4py = LoggingPorter()
        fc = FileInspector()
        boolean = fc.is_has_file("owl-appium.ini")
        if boolean: 
            self.__fileabspath = fc.get_file_abspath()
            self.__projectpath = fc.get_project_path()
        self.cf = ConfigReader(self.__fileabspath)

    @property
    def properties(self):
        """
        获取配置文件中的内容并返回对应的对象
        :return:
        """
        ap = AppiumIniDomain()
        try:
            ap.pageLoadTimeout = self.cf.get_value("TimeSet", "pageLoadTimeout")
            ap.waitTimeout = self.cf.get_value("TimeSet", "waitTimeout")
            ap.scriptTimeout = self.cf.get_value("TimeSet", "scriptTimeout")
            ap.pauseTime = self.cf.get_value("TimeSet", "pauseTime")

            ap.capturePath = os.path.join(self.__projectpath, self.cf.get_value("ResultPath", "capturePath"))
            if not os.path.exists(ap.capturePath):
                os.makedirs(ap.capturePath)
            ap.htmlreportPath = os.path.join(self.__projectpath, self.cf.get_value("ResultPath", "htmlreportPath"))
            if not os.path.exists(ap.htmlreportPath):
                os.makedirs(ap.htmlreportPath)
            ap.dumpxmlPath = os.path.join(self.__projectpath, self.cf.get_value("ResultPath", "dumpxmlPath"))
            if not os.path.exists(ap.dumpxmlPath):
                os.makedirs(ap.dumpxmlPath)
            ap.appiumlogPath = os.path.join(self.__projectpath, self.cf.get_value("ResultPath", "appiumlogPath"))
            if not os.path.exists(ap.appiumlogPath):
                os.makedirs(ap.appiumlogPath)
            ap.permissionPath = os.path.join(self.__projectpath, self.cf.get_value("ResultPath", "permissionPath"))
            if not os.path.exists(ap.permissionPath):
                os.makedirs(ap.permissionPath)
            ap.appiumService = os.path.join(self.__projectpath, self.cf.get_value("ResultPath", "appiumService"))

        except Exception as e:
            self.log4py.error("实例化appium配置文件对象时，出现异常 ：" + str(e))
        return ap

    def get_run_conf(self):
        section = "run"
        try:
            # 是否是第一次跑，或者是重新跑，为0时会重新安装指定apk，并执行任务；为1时直接启动安装的app进行任务操作
            is_first = self.cf.get_value(section, "isFirst")
            # app的包名
            pkg_name = self.cf.get_value(section, "pkgName")
            # 启动app的main activity
            launch_activity = self.cf.get_value(section, "launchActivity")
            # 自动化启动app时，需要这个等待来做缓冲，避免启动页面挡住操作
            wait_activity = self.cf.get_value(section, "waitActivity")
            # 到isFirst为0时，就进行安装操作
            apk_file_path = self.cf.get_value(section, "apkFilePath")
        except Exception as e:
            return None
        return {"is_first": is_first, "pkg_name": pkg_name, "launch_activity": launch_activity, "wait_activity": wait_activity, "apk_file_path": apk_file_path}

    def set_run_conf(self, is_first, pkg_name, launch_activity, wait_activity, apk_file_path):
        flag = False
        section = "run"
        try:
            self.cf.set_value(section, "isFirst", is_first)
            self.cf.set_value(section, "pkgName", pkg_name)
            self.cf.set_value(section, "launchActivity", launch_activity)
            self.cf.set_value(section, "waitActivity", wait_activity)
            self.cf.set_value(section, "apkFilePath", apk_file_path)
            flag = True
        except Exception as e:
            return None
        return flag

    def get_desired_caps_conf(self):
        section = "desired_caps"
        # 这些参数都是启动app时需要的，但是在代码读取参数的时候，不一定都读取，因为有些参数不是固定的
        dc = {}
        try:
            dc["automationName"] = self.cf.get_value(section, "automationName")
            dc["platformName"] = self.cf.get_value(section, "platformName")
            # dc["app"] = self.cf.get(section, "app")
            dc["appPackage"] = self.cf.get_value(section, "appPackage")
            dc["appActivity"] = self.cf.get_value(section, "appActivity")
            dc["noSign"] = self.cf.get_value(section, "noSign")
            dc["unicodeKeyboard"] = self.cf.get_value(section, "unicodeKeyboard")
            dc["resetKeyboard"] = self.cf.get_value(section, "resetKeyboard")
        except Exception as e:
            return None
        return dc