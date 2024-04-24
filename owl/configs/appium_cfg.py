# -*- coding: utf-8 -*-

"""
@author: jayzhen
@license: Apache Licence 
@version: Python 3.8+
@file: appium_cfg.py
@time: 2024/4/1 10:40
"""


import os

from owl.configs import BaseOwlConfiger
from owl.domain.appium_config_do import AppiumConfigDomain
from owl.lib.processor.config_processor import ConfigControl


class AppiumConfiger(BaseOwlConfiger):
    """
    读取配置文件.conf的内容，返回driver的绝对路径
    """

    def __init__(self):
        super().__init__()

    def __validator_path(self, section, key):
        file_path = os.path.join(self.__project_root_path, self.cfg.get_value(section, key))
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        return file_path

    @property
    def properties(self):
        """
        获取配置文件中的内容并返回对应的对象
        :return:
        """
        ap = AppiumConfigDomain()
        try:
            section = "appium.run"
            ap.isAutoStartAppiumService = self.cfg.get_boolean(section, 'isAutoStartAppiumService')
            ap.pageLoadTimeout = self.cfg.get_value(section, "pageLoadTimeout")
            ap.waitTimeout = self.cfg.get_value(section, "waitTimeout")
            ap.scriptTimeout = self.cfg.get_value(section, "scriptTimeout")
            ap.pauseTime = self.cfg.get_value(section, "pauseTime")

            ap.capturePath = self.__validator_path(section, "capturePath")
            ap.htmlReportPath = self.__validator_path(section,  "htmlReportPath")
            ap.dumpxmlPath = self.__validator_path(section,  "dumpxmlPath")
            ap.appiumLogPath = self.__validator_path(section,  "appiumlogPath")
            ap.permissionPath = self.__validator_path(section, "permissionPath")
            ap.appiumService = os.path.join(self.__project_root_path, self.cfg.get_value(section, "appiumService"))
        except Exception as e:
            self.log4py.error("实例化appium配置文件对象时，出现异常 ：" + str(e))
        return ap

    def get_run_conf(self):
        section = "appium.run"
        # 是否是第一次跑，或者是重新跑，为0时会重新安装指定apk，并执行任务；为1时直接启动安装的app进行任务操作
        is_first = self.cfg.get_boolean(section, "isFirst")
        # app的包名
        pkg_name = self.cfg.get_value(section, "pkgName")
        # 启动app的main activity
        launch_activity = self.cfg.get_value(section, "launchActivity")
        # 自动化启动app时，需要这个等待来做缓冲，避免启动页面挡住操作
        wait_activity = self.cfg.get_value(section, "waitActivity")
        # 到isFirst为0时，就进行安装操作
        apk_file_path = self.cfg.get_value(section, "apkFilePath")
        # @TODO 这个需要优化
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
        section = "appium.run"
        try:
            self.cfg.set_value(section, "isFirst", is_first)
            self.cfg.set_value(section, "pkgName", pkg_name)
            self.cfg.set_value(section, "launchActivity", launch_activity)
            self.cfg.set_value(section, "waitActivity", wait_activity)
            self.cfg.set_value(section, "apkFilePath", apk_file_path)
            flag = True
        except Exception as e:
            return flag
        return flag

    def get_desired_caps_conf(self):
        section = "appium.driver"
        # 这些参数都是启动app时需要的，但是在代码读取参数的时候，不一定都读取，因为有些参数不是固定的
        dc = {
            "automationName": self.cfg.get_value(section, "automationName"),
            "platformName": self.cfg.get_value(section, "platformName"),
            "appPackage": self.cfg.get_value(section, "appPackage"),
            "appActivity": self.cfg.get_value(section, "appActivity"),
            "noSign": self.cfg.ini_reader.getboolean(section, "noSign"),
            "unicodeKeyboard": self.cfg.ini_reader.getboolean(section, "unicodeKeyboard"),
            "resetKeyboard": self.cfg.ini_reader.getboolean(section, "resetKeyboard"),
        }
        # dc["app"] = self.cf.get(section, "app")
        return dc


PATH = lambda a: os.path.abspath(a)


class AppiumServiceConfiger(BaseOwlConfiger):
    """
    1.该类主要处理appium多机并发测试场景下生成的端口与机器的设备号映射。
    a.接受初始化service中接受到device_list和service_list
    b.先判断是否存在固定的config文件，如果没有就创建；有，就覆盖模式进行写入
    c.循环遍历这个list并写入文件中
    """

    def __init__(self):
        super().__init__()
        self.appium_service_cfg_path = os.path.join(self.__project_root_path, self.cfg.get_value("appium.run", "appiumService"))

    def set_appium_uuids_ports(self, devices, ports):
        """
        遍历list,按照下表进行对应映射
        :param devices: 手机uuid
        :param ports: pc启动的appium服务端口
        """
        bol = self.create_config_file(self.appium_service_cfg_path)
        if bol:
            self.log4py.info("创建文件成功：{}".format(self.appium_service_cfg_path))
            ap = ConfigControl(self.appium_service_cfg_path)
            if len(devices) > 0 and len(ports) > 0:
                for i in range(len(devices)):
                    filed = devices[i]
                    key = filed
                    value = ports[i]
                    # 因为是覆盖写入，没有section，需要先添加再设置, 初始化的服务都加一个run的标识
                    ap.add_section_key_value(filed, key, value)
                    ap.set_value(filed, "run", "0")
                    self.log4py.debug(
                        "设备sno与appium服务端口映射已写入配置文件:{}--{}".format(key, value))
                ap.flush()

    def set_appium_uuid_port(self, device, port):
        """
        如果这样一个一个的写入到配置文件中，是追加还是覆盖？如果是覆盖的，服务启动完成后就剩一个配置，所以不行
        如果是追加，需要判断配置文件中是否已经有了相同的section，有就更新，没有就添加
        :param device: 手机uuid
        :param port pc启动的appium服务端口
        """
        bol = self.create_config_file(self.appium_service_cfg_path)
        if bol:
            if device is not None and port is not None:
                ap = ConfigControl(self.appium_service_cfg_path)
                sec = device
                key = device
                value = port
                if ap.had_section(sec):
                    ap.set_value(sec, key, value)
                    ap.set_value(sec, "run", "0")
                else:
                    ap.add_section_key_value(sec, key, value)
                    ap.set_value(sec, "run", "0")
                ap.flush()
                self.log4py.debug(
                    "设备 sno 与 appium 服务端口映射已写入配置文件: {}={}".format(key, value))

    def get_all_appium_server_port(self):
        port_list = []
        if os.path.exists(self.appium_service_cfg_path):
            asp = ConfigControl(self.appium_service_cfg_path)
            section_list = asp.get_sections()
            for sl in section_list:
                port_list.append(asp.get_value(sl, sl))
        return port_list

    def get_appium_log_path(self):
        path = os.path.join(self.__project_root_path, self.cfg.get_value("appium.run", "appiumLogPath"))
        if PATH(path):
            if not os.path.exists(path):
                os.makedirs(path)
            self.log4py.info("获取到appium服务的日志绝对路径 %s" % path)
            return path.replace("\\", "/")
        return None
