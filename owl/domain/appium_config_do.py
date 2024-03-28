# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@software: PyCharm
@file: AppiumIniDomain
@time: 2018/4/8  18:08
"""


class AppiumIniDomain(object):

    def __init__(self):
        # 页面加载等待时间，单位：秒
        self.pageLoadTimeout = 0
        # 定位元素等待时间，单位：秒
        self.waitTimeout = 0
        # 异步加载等待时间
        self.scriptTimeout = 0
        # 单位：毫秒
        self.pauseTime = 0
        # 截图保存的路径
        self.capturePath = None
        # html报告路径
        self.htmlReportPath = None
        # appium服务的日志路径
        self.appiumLogPath = None
        # 保存页面的xml文件路径
        self.dumpxmlPath = None
        # appium服务启动后的端口记录文件
        self.appiumService = None
        # 手机权限配置文件
        self.permissionPath = None

    def __str__(self):
        return "页面加载等待时间，单位：秒 :" + str(self.pageLoadTimeout) + \
               " ;\n定位元素等待时间，单位：秒 :" + str(self.waitTimeout) + \
               " ;\n异步加载等待时间 : " + str(self.scriptTimeout) + \
               " ;\n延迟时间，单位：毫秒： " + str(self.pauseTime) + \
               " ;\n截图保存的路径 : " + str(self.capturePath) + \
               " ;\nhtml报告路径 : " + str(self.htmlReportPath) + \
               " ;\n日志路径 : " + str(self.appiumLogPath) + \
               " ;\n保存的页面xml文件 :" + str(self.dumpxmlPath)
