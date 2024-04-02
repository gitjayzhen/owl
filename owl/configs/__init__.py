# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@file: __init__.py.py
"""
import os

from owl.exception.owl_type import SingletonInstantiationException
from owl.lib.file.config_resolver import ConfigControl
from owl.lib.file.file_inspector import FileInspector
from owl.lib.reporter.logging_porter import LoggingPorter


class ConfigReader:
    __instance = None

    @staticmethod
    def get_instance():
        if not ConfigReader.__instance:
            ConfigReader()
        return ConfigReader.__instance

    def __init__(self):
        if ConfigReader.__instance:
            raise SingletonInstantiationException()
        else:
            ConfigReader.__instance = self
            fc = FileInspector()
            boolean = fc.is_has_file("owl.ini")
            if boolean:
                self.__file_abs_path = fc.get_file_abspath()
                self.__project_path = fc.get_project_path()
            self.conf = ConfigControl(self.__file_abs_path)

    def get_redis_config(self):
        return {
            'host': self.conf.ini_reader.get('db.redis', 'host'),
            'port': self.conf.ini_reader.getint('db.redis', 'port'),
            'db': self.conf.ini_reader.getint('db.redis', 'db'),
            'passwd': self.conf.ini_reader.get('db.redis', 'passwd')
        }

    def get_mysql_config(self):
        # 获取数据库连接信息
        return {
            'host': self.conf.ini_reader.get('db.mysql', 'host'),
            'port': self.conf.ini_reader.getint('db.mysql', 'port'),
            'database': self.conf.ini_reader.get('db.mysql', 'database'),
            'user': self.conf.ini_reader.get('db.mysql', 'user'),
            'password': self.conf.ini_reader.get('db.mysql', 'password')
        }


class BaseOwlConfiger(object):

    def __init__(self):
        self.__base_owl_cfg_name = "owl.ini"
        self.__cfg_path = None
        self.__project_root_path = None
        self.log4py = LoggingPorter()
        self.fc = FileInspector()
        if self.fc.is_has_file(self.__base_owl_cfg_name):
            self.__cfg_path = self.fc.get_file_abspath()
            self.__project_root_path = self.fc.get_project_path()
            if "tests" in self.__project_root_path:
                self.project_root_path = os.path.join(self.__project_root_path.split("tests")[0], "/tests")
        else:
            raise FileNotFoundError(f"{self.__base_owl_cfg_name} is not found")
        self.cfg = ConfigControl(self.__cfg_path)

    @property
    def properties(self):
        return None

    @classmethod
    def is_absolute_and_exists(cls, path):
        if os.path.isabs(path) and os.path.exists(path):
            return True
        return False

    @classmethod
    def get_file_path(cls, prop_path, env_key):
        if not cls.is_absolute_and_exists(prop_path):
            return os.environ.get(env_key)
        return prop_path

    @classmethod
    def create_config_file(cls, path):
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
