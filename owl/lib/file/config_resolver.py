# -*- encoding: utf-8 -*-

"""
@author: jayzhen 
@license: Apache Licence
@file: ConfigPaserUtil.py
@time: 2017/7/26 16:19
"""
import os
from configparser import ConfigParser

from owl.lib.reporter.logging_porter import LoggingPorter


class ConfigControl(object):

    def __init__(self, file_path):
        self.log4py = LoggingPorter()
        if not os.path.exists(file_path):
            assert FileNotFoundError("{} 文件不存在".format(file_path))
        self.ini_reader = ConfigParser()
        self.ini_reader.read(file_path)
        self.file_path = file_path

    def flush(self):
        self.ini_reader.write(open(self.file_path, 'w+'))
        self.log4py.info("已将内容写入了 {} 配置文件中".format(str(os.path.basename(self.file_path))))

    def had_section(self, section):
        return self.ini_reader.has_section(section)

    def had_option(self, section, option):
        return self.ini_reader.has_option(section, option)

    def get_sections(self):
        try:
            return self.ini_reader.sections()
        except Exception as e:
            self.log4py.error("获取ini文件的所有section时，发生错误：{}".format(str(e)).decode("utf-8"))

    def get_section_items(self, section):
        if section is None or section == " ":
            return None
        try:
            values = self.ini_reader.items(section)
            return values
        except Exception as e:
            self.log4py.error("获取节点的所有key:value(items)时出错:{}".format(str(e)).decode("utf-8"))

    def get_value(self, section, key):
        if section is None or section == " ":
            return None
        if key is None or key == " ":
            return None
        try:
            value = self.ini_reader.get(section, key)
            return value
        except Exception as e:
            self.log4py.error("获取配置文件的 key 的 value 发生错误: {}".format(e))
            return None

    def set_value(self, section, key, value):
        flag = False
        if section is None or section == " ":
            return flag
        if key is None or key == " ":
            return flag
        try:
            self.ini_reader.set(str(section), str(key), str(value))
            # self.ini_reader.write(self.file_path)
            flag = True
        except Exception as e:
            self.log4py.error("设置已有的 key 的 value 发生错误: {}".format(str(e)))
        return flag

    def add_section_key_value(self, section, key, value):
        flag = False
        if section is None or section == " ":
            return flag
        if key is None or key == " ":
            return flag
        if value is None:
            value = " "
        try:
            self.ini_reader.add_section(section)
            flag = self.set_value(section, key, value)
        except Exception as e:
            self.log4py.error("设置已有的key的value发生错误: {}".format(str(e)))
        return flag
