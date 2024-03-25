# -*- coding:UTF-8 -*-

"""
@author: jay.zhen
@time: 2024/3/25  13:12
"""

import datetime
import operator
import os
import time

from owl.lib.decorator import deprecated
from owl.lib.reporter.logging_porter import LoggingPorter


class FileInspector(object):
    """
        1.通过filecheck来查看项目目录下是否有指定文件;
        2.确定有指定文件后，可以获取文件的绝对路径（一定要保证文件名是正确的）
    """

    def __init__(self, filename=None, is_parent_lookup=True):
        self.__file_abs_path = None  # 不可访问的
        self.__filename = filename
        self.__is_parent_lookup = is_parent_lookup
        self.ignore_dir = {".idea", ".git", "__pycache__", '__init__.py', '.pytest_cache', 'doc'}
        # 可以基于允许入口的路径进行查找说需要的文件
        self.__runtime_path = os.getcwd()
        self.log4py = LoggingPorter()

    def is_has_file(self, file_name):
        """
        是否存在指定的文件，路径默认为当前项目的目录
        :param file_name:  文件名
        :return:  True or False
        """
        if file_name is None and self.__filename is not None:
            file_name = self.__filename
        # 基于当前运行目录下是否有所需要的文件
        result = self.is_path_has_file(self.__runtime_path, file_name)
        if not result and self.__is_parent_lookup:
            # 程序运行入口向外再查找一层
            self.ignore_dir.add(os.path.basename(self.__runtime_path))
            result = self.is_path_has_file(os.path.dirname(self.__runtime_path), file_name)
        return result

    def is_path_has_file(self, path, filename):
        """指定目录下是否存在指定的文件"""
        return self.check_has_file(path, filename)

    def check_has_file(self, path, filename):
        """   扫描指定目录下的所有文件，找到所要找的文件，return True or False"""
        try:
            for filep, dirs, filelist in os.walk(path):
                if os.path.basename(filep) in self.ignore_dir:
                    # self.log4py.debug("跳过这个目录的检索工作：[{}]".format(str(filep)))
                    continue
                for fl in filelist:
                    if operator.eq(fl, filename):
                        self.__file_abs_path = os.path.join(filep, fl)
                        self.log4py.info("当前项目下查找的[%s]配置文件存在." % filename)
                        return True
            return False
        except Exception as e:
            self.log4py.error("check_has_file()方法出现异常" + str(e))
            return False

    def get_file_abspath(self):
        """获取文件的绝对路径之倩需要check文件是否存在"""
        return self.__file_abs_path

    @deprecated
    def get_project_path(self):
        """ 截取当前项目所有在的路径 """
        # @Warning 这个逻辑不合适
        # project_path = self.__runtime_path.split("owl")[0]  # 当前项目的代码目录节点，通过他来知道项目根目录
        # return os.path.join(project_path, "owl/")
        return self.__runtime_path

    def get_latest_file(self, absolute_path='./'):
        """
        1.在指定文件下，获取所有文件
        2.再获取每个文件的时间，对比后获取文件名（使用内置函数）
        :param absolute_path: 绝对路径，默认是当前目录
        :return: 文件路径，最新文件名，绝对路径
        """
        l = os.listdir(absolute_path)  # 该目录下的文件list
        # 对key进行升序排列（变量fn是每个文件或者文件夹的全称，如果fn是不是文件夹或者是0，那就获取该文件的创建时间，排序后的最后一个文件就是最新的文件了）
        # 第二句
        st = l.sort(key=lambda fn: os.path.getmtime(absolute_path + "\\" + fn) if not os.path.isdir(
            absolute_path + "\\" + fn) else 0)
        d = datetime.datetime.fromtimestamp(os.path.getmtime(absolute_path + "\\" + l[-1]))
        fname = l[-1]
        fpath = os.path.join(absolute_path, fname)
        self.log4py.debug('last file is ::' + fpath)
        time_end = time.mktime(d.timetuple())
        self.log4py.debug('time_end:%s' % time_end)
        # fpath:html文件的全目录,fname：最新html文件名,relative_path：html文件当前所处文件夹路径
        return fpath, fname, absolute_path
