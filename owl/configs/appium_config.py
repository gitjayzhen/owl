# -*- coding:UTF-8 -*-
"""
Created on 2016年4月26日
@author: jayzhen
"""

import os
from owl.lib.file.config_resolver import ConfigControl
from owl.lib.file.file_inspector import FileInspector
from owl.domain.appium_config_do import AppiumIniDomain
from owl.lib.reporter.logging_porter import LoggingPorter


class AppiumConfiger(object):
    """
    读取配置文件.conf的内容，返回driver的绝对路径
    """

    def __init__(self):
        self.config_path = None
        self.project_root_path = None
        self.log4py = LoggingPorter()
        fc = FileInspector()
        boolean = fc.is_has_file("owl-appium.ini")
        if boolean:
            self.config_path = fc.get_file_abspath()
            self.project_root_path = fc.get_project_path()
        else:
            raise FileNotFoundError("owl-appium.ini is not found")
        self.cfg = ConfigControl(self.config_path)

    @property
    def properties(self):
        """
        获取配置文件中的内容并返回对应的对象
        :return:
        """
        ap = AppiumIniDomain()
        try:
            ap.pageLoadTimeout = self.cfg.get_value("TimeSet", "pageLoadTimeout")
            ap.waitTimeout = self.cfg.get_value("TimeSet", "waitTimeout")
            ap.scriptTimeout = self.cfg.get_value("TimeSet", "scriptTimeout")
            ap.pauseTime = self.cfg.get_value("TimeSet", "pauseTime")

            ap.capturePath = os.path.join(self.project_root_path, self.cfg.get_value("ResultPath", "capturePath"))
            if not os.path.exists(ap.capturePath):
                os.makedirs(ap.capturePath)
            ap.htmlreportPath = os.path.join(self.project_root_path, self.cfg.get_value("ResultPath", "htmlreportPath"))
            if not os.path.exists(ap.htmlreportPath):
                os.makedirs(ap.htmlreportPath)
            ap.dumpxmlPath = os.path.join(self.project_root_path, self.cfg.get_value("ResultPath", "dumpxmlPath"))
            if not os.path.exists(ap.dumpxmlPath):
                os.makedirs(ap.dumpxmlPath)
            ap.appiumlogPath = os.path.join(self.project_root_path, self.cfg.get_value("ResultPath", "appiumlogPath"))
            if not os.path.exists(ap.appiumlogPath):
                os.makedirs(ap.appiumlogPath)
            ap.permissionPath = os.path.join(self.project_root_path, self.cfg.get_value("ResultPath", "permissionPath"))
            if not os.path.exists(ap.permissionPath):
                os.makedirs(ap.permissionPath)
            ap.appiumService = os.path.join(self.project_root_path, self.cfg.get_value("ResultPath", "appiumService"))

        except Exception as e:
            self.log4py.error("实例化appium配置文件对象时，出现异常 ：" + str(e))
        return ap

    def get_run_conf(self):
        section = "run"
        # 是否是第一次跑，或者是重新跑，为0时会重新安装指定apk，并执行任务；为1时直接启动安装的app进行任务操作
        is_first = self.cfg.get_value(section, "isFirst")
        # app的包名
        pkg_name = self.cfg.get_value(section, "pkgName")
        # 启动app的main activity
        launch_activity = self.cfg.get_value(section, "launchActivity")
        # 自动化启动app时，需要这个等待来做缓冲，避免启动页面挡住操作
        wait_activity = self.cfg.get_value(section, "waitActivity")
        # 到isFirst为0时，就进行安装操作
        apk_file_path = self.cfg.get_value(section, "apkFilePath")
        if not os.path.isabs(apk_file_path):
            base = os.getcwd()
            base = os.path.join((base.split('owl'))[0], 'owl')
            apk_file_path = os.path.join(base, apk_file_path)
        result = {
                "is_first": is_first,
                "pkg_name": pkg_name,
                "launch_activity": launch_activity,
                "wait_activity": wait_activity,
                "apk_file_path": apk_file_path
            }
        return result

    def set_run_conf(self, is_first, pkg_name, launch_activity, wait_activity, apk_file_path):
        flag = False
        section = "run"
        try:
            self.cfg.set_value(section, "isFirst", is_first)
            self.cfg.set_value(section, "pkgName", pkg_name)
            self.cfg.set_value(section, "launchActivity", launch_activity)
            self.cfg.set_value(section, "waitActivity", wait_activity)
            self.cfg.set_value(section, "apkFilePath", apk_file_path)
            flag = True
        except Exception as e:
            return None
        return flag

    def get_desired_caps_conf(self):
        section = "desired_caps"
        # 这些参数都是启动app时需要的，但是在代码读取参数的时候，不一定都读取，因为有些参数不是固定的
        dc = {
            "automationName": self.cfg.get_value(section, "automationName"),
            "platformName": self.cfg.get_value(section, "platformName"),
            "appPackage": self.cfg.get_value(section, "appPackage"),
            "appActivity": self.cfg.get_value(section, "appActivity"),
            "noSign": self.cfg.get_value(section, "noSign"),
            "unicodeKeyboard": self.cfg.get_value(section, "unicodeKeyboard"),
            "resetKeyboard": self.cfg.get_value(section, "resetKeyboard")
        }
        # dc["app"] = self.cf.get(section, "app")
        return dc


PATH = lambda a: os.path.abspath(a)


class AppiumServerConfigFile(object):
    """
    1.该类主要处理appium多机并发测试场景下生成的端口与机器的设备号映射。
    a.接受初始化service中接受到device_list和service_list
    b.先判断是否存在固定的config文件，如果没有就创建；有，就覆盖模式进行写入
    c.循环遍历这个list并写入文件中
    """

    def __init__(self):
        self.fi = FileInspector()
        if self.fi.is_has_file("owl-appium.ini"):
            fp = self.fi.get_file_abspath()
            self.cfg = ConfigControl(fp)
        self.log4py = LoggingPorter()
        self.log4py.info("-----配置文件操作开始-----")
        self.f_path = os.path.join(self.fi.get_project_path(), self.cfg.get_value("ResultPath", "appiumService"))

    def __del__(self):
        self.log4py.info("-----配置文件操作结束-----")

    def set_appium_uuids_ports(self, devices, ports):
        """
        遍历list,按照下表进行对应映射
        :param devices: 手机uuid
        :param ports: pc启动的appium服务端口
        """
        bol = self.create_config_file(self.f_path)
        if bol:
            self.log4py.info("创建appiumService.ini文件成功：{}".format(self.f_path))
            ap = ConfigControl(self.f_path)
            if len(devices) > 0 and len(ports) > 0:
                for i in range(len(devices)):
                    filed = devices[i]
                    key = filed
                    value = ports[i]
                    # 因为是覆盖写入，没有section，需要先添加再设置, 初始化的服务都加一个run的标识
                    ap.add_section_key_value(filed, key, value)
                    ap.set_value(filed, "run", "0")
                    self.log4py.debug("设备sno与appium服务端口映射已写入appiumService.ini配置文件:{}--{}".format(key, value))
                ap.flush()

    def set_appium_uuid_port(self, device, port, bp):
        """
        如果这样一个一个的写入到配置文件中，是追加还是覆盖？如果是覆盖的，服务启动完成后就剩一个配置，所以不行
        如果是追加，需要判断配置文件中是否已经有了相同的section，有就更新，没有就添加
        :param device: 手机uuid
        :param port pc启动的appium服务端口
        """
        bol = self.create_config_file(self.f_path)
        if bol:
            if device is not None and port is not None:
                ap = ConfigControl(self.f_path)
                sec = device
                key = device
                value = port
                if ap.had_section(sec):
                    ap.set_value(sec, key, value)
                    ap.set_value(sec, "bp", bp)
                    ap.set_value(sec, "run", "0")
                else:
                    ap.add_section_key_value(sec, key, value)
                    ap.set_value(sec, "bp", bp)
                    ap.set_value(sec, "run", "0")
                ap.flush()
                self.log4py.debug("设备sno与appium服务端口映射已写入appiumService.ini配置文件:{}--{}".format(key, value))

    def create_config_file(self, path):
        """
        如果path这个文件不存在，就创建这个文件;存在就清空文件
        :param path: 是一个文件的绝对路径
        :return:
        """
        if os.path.exists(path) and os.path.isfile(path):
            return True
        dir_name = os.path.dirname(path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        f = open(path, "w+")
        f.close()
        if os.path.exists(path) and os.path.isfile(path):
            return True
        return False

    def get_all_appium_server_port(self):

        port_list = []
        if os.path.exists(self.f_path):
            ap = ConfigControl(self.f_path)
            section_list = ap.get_sections()
            for sl in section_list:
                port_list.append(ap.get_value(sl, sl))
                port_list.append(ap.get_value(sl, "bp"))
        return port_list

    def get_appium_logs_path(self):
        path = os.path.join(self.fi.get_project_path(), self.cfg.get_value("ResultPath", "appiumlogPath"))
        if PATH(path):
            if not os.path.exists(path):
                os.makedirs(path)
            self.log4py.info("获取到appium服务的日志绝对路径 %s" % path)
            return path.replace("\\", "/")
        return None