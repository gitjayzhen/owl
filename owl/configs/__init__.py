# -*- coding: utf-8 -*-

"""
@version: v1.0
@author: jayzhen
@file: __init__.py.py
"""

from owl.exception.owl_type import SingletonInstantiationException
from owl.lib.file.config_resolver import ConfigControl
from owl.lib.file.file_inspector import FileInspector


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
