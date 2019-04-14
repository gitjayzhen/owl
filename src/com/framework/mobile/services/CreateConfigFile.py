#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version: python2.7
@author: ‘jayzhen‘
@contact: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm Community Edition
1.该类主要处理appium多机并发测试场景下生成的端口与机器的设备号映射。
a.接受初始化service中接受到device_list和service_list
b.先判断是否存在固定的config文件，如果没有就创建；有，就覆盖模式进行写入
c.循环遍历这个list并写入文件中
"""
import os
from com.framework.utils.reporterUtil.LoggingPorter import LoggingPorter
from com.framework.utils.fileUtil.FileInspector import FileInspector
from com.framework.utils.fileUtil.ConfigReader import ConfigReader

PATH = lambda a: os.path.abspath(a)


class CreateConfigFile(object):

    def __init__(self):
        self.fkctl = FileInspector()

        if self.fkctl.is_has_file("owl-appium.ini"):
            fp = self.fkctl.get_file_abspath()
            self.cfg = ConfigReader(fp)
        self.log4py = LoggingPorter()
        self.log4py.info("-----配置文件操作开始-----")
        self.f_path = os.path.join(self.fkctl.get_project_path(), self.cfg.get_value("ResultPath", "appiumService"))

    def __del__(self):
        self.log4py.info("-----配置文件操作结束-----")

    def set_appium_uuids_ports(self, device_list, port_list):
        """
        遍历list,按照下表进行对应映射
        :param device_lsit: 手机uuid
        :param port_list: pc启动的appium服务端口
        """
        bol = self.create_config_file(self.f_path)
        if bol:
            self.log4py.info("创建appiumService.ini文件成功：{}".format(self.f_path))
            ap = ConfigReader(self.f_path)
            if len(device_list) > 0 and len(port_list) > 0:
                for i in range(len(device_list)):
                    filed = device_list[i]
                    key = filed
                    value = port_list[i]
                    # 因为是覆盖写入，没有section，需要先添加再设置, 初始化的服务都加一个run的标识
                    ap.add_section_key_value(filed, key, value)
                    ap.set_value(filed, "run", "0")
                ap.flush()
                self.log4py.debug("设备sno与appium服务端口映射已写入appiumService.ini配置文件:{}--{}".format(key, value))

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
                ap = ConfigReader(self.f_path)
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
        f = open(path, "wb")
        f.close()
        if os.path.exists(path) and os.path.isfile(path):
            return True
        return False

    def get_all_appium_server_port(self):

        port_list = []
        if os.path.exists(self.f_path):
            ap = ConfigReader(self.f_path)
            section_list = ap.get_sections()
            for sl in section_list:
                port_list.append(ap.get_value(sl, sl))
                port_list.append(ap.get_value(sl, "bp"))
        return port_list

    def get_appium_logs_path(self):
        path = os.path.join(self.fkctl.get_project_path(), self.cfg.get_value("ResultPath", "appiumlogPath"))
        if PATH(path):
            if not os.path.exists(path):
                os.makedirs(path)
            self.log4py.info("获取到appium服务的日志绝对路径 %s" % path)
            return path.replace("\\", "/")
        return None

