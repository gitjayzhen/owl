# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@license: Apache Licence 
@message: jayzhen_testing@163.com
@software: PyCharm
@file: se_config_do.py
@time: 2023/8/16 12:49
"""


class SeleniumIniDomain(object):

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
        self.htmlreportPath = None
        self.logsPath = None
        # 浏览器初始化界面URL
        self.baseURL = None
        # 测试的时候需要使用哪个浏览器，就配置成那个
        self.browser = None
        # run那个浏览器 就取那个浏览器的驱动
        self.browserdriver = None
        # 执行浏览器的type
        self.type = None
        # 远程访问浏览器的配置:{}
        self.remoteProfile = None
        # 是否使用无头模式
        self.isHeadless = False

    def __str__(self):
        return "页面加载等待时间，单位：秒 :" + str(self.pageLoadTimeout) + \
               " ;\n定位元素等待时间，单位：秒 :" + str(self.waitTimeout) + \
               " ;\n异步加载等待时间 : " + str(self.scriptTimeout) + \
               " ;\n延迟时间，单位：毫秒： " + str(self.pauseTime) + \
               " ;\n截图保存的路径 : " + str(self.capturePath) + \
               " ;\nhtml报告路径 : " + str(self.htmlreportPath) + \
               " ;\n日志路径 : " + str(self.logsPath) + \
               " ;\n浏览器初始化界面URL :" + str(self.baseURL) + \
               " ;\n启动的浏览器 : " + str(self.browser) + \
               " ;\nrun那个浏览器 就取那个浏览器的驱动 : " + str(self.browserdriver) + \
               " ;\n执行本地浏览器还是远程浏览器 ： " + str(self.type) + \
               " ;\n远程浏览器配置 : " + str(self.remoteProfile)
