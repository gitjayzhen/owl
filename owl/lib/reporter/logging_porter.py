# -*- coding:utf8 -*-

"""
@author: jayzhen
@time: 2024/3/22  13:12
该日志类可以把不同级别的日志输出到不同的日志文件中

1. 日志对象
2. 这对象需要有对于的处理器，决定将日志输出到什么地方
3. 这个处理器又需要设置对应的 日志等级、日志格式
"""

import os
import datetime
import logging
import inspect
import platform

from owl.lib.decorator import singleton

# 关于这个路径有两个选择，完全使用一个相对路径，或者使用一个配置方式，然后两者设置优先级
pwd = os.getcwd()
if "tests" in pwd:
    pwd = os.path.join(pwd.split("tests")[0], "tests")
LOG_FILE_PATH = os.path.join(pwd, "logs")
if not os.path.exists(LOG_FILE_PATH):
    os.makedirs(LOG_FILE_PATH)

# 将对应文件实例化成一个FileHandler对象，让不用级别的日志共用该Filehandler，这样做到日志打印到一个文件中
hd = logging.FileHandler(os.path.abspath(os.path.join(LOG_FILE_PATH, "owl.log")))
hds = logging.StreamHandler()
handlers = {logging.DEBUG: [hd, hds], logging.INFO: [hd, hds], logging.WARNING: [hd, hds], logging.ERROR: [hd, hds]}


@singleton
class LoggingPorter(object):
    """
    日志文档
    """
    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}
        log_levels = handlers.keys()
        for level in log_levels:
            logger = logging.getLogger(str(level))
            logger.addHandler(handlers[level][0])
            logger.addHandler(handlers[level][1])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def __del__(self):
        hd.close()

    def get_log_message(self, level, message):
        """日志格式：[时间] [类型] [记录代码] 信息"""
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        try:
            relative_path = filename.split("owl")[-1]
            system = platform.system()
            if system == "Windows":
                relative_path = relative_path.replace("\\", ".")
            elif system == "Linux" or system == "Darwin":
                relative_path = relative_path.replace("/", ".")
            relative_path = relative_path.replace(".", "", 1)
        except IndexError as ie:
            print("日志获取当前脚本的绝对路径发生了错误{}".format(str(ie)))
            relative_path = filename
        return "%s [%s] %s(%s) - %s" % (
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f'),
            level, relative_path, lineNo, message)

    def info(self, message):
        message = self.get_log_message("INFO", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.get_log_message("ERROR", message)
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.get_log_message("WARNING", message)
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.get_log_message("DEBUG", message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.get_log_message("CRITICAL", message)
        self.__loggers[logging.CRITICAL].critical(message)


@singleton
class LoggingPorterWithConfig(object):

    def __init__(self):
        pro_root = os.getcwd()
        f_path = os.path.join(pro_root, "logging.conf")
        logging.config.fileConfig(f_path)    # 采用配置文件
        logging.basicConfig()
        # create logger  debug,info,warning,error
        self.D = logging.getLogger("debug")
        self.I = logging.getLogger("info")
        self.W = logging.getLogger("warning")
        self.E = logging.getLogger("error")

    def get_message(self, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s- %s -%s] %s" % (filename, lineNo, functionName, message)

    def debug(self, mag):
        mag = self.get_message(mag)
        # print(self.D.handlers)
        self.D.debug(mag)

    def info(self, mag):
        mag = self.get_message(mag)
        # print(self.I.handlers)
        self.I.info(mag)

    def warn(self, mag):
        mag = self.get_message(mag)
        # print(self.W.handlers)
        self.W.warning(mag)

    def error(self, mag):
        mag = self.get_message(mag)
        # print(self.E.handlers)
        self.E.error(mag)


if __name__ == '__main__':
    log = LoggingPorterWithConfig()
    log.info("testing1")
    log.debug("testing2")
    log.warn("testing3")
    log.error("testing4")