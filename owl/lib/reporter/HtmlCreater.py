# -*- coding:UTF-8 -*-
"""
@version: python2.7
@author: ‘jayzhen‘
@contact: jayzhen_testing@163.com
@site: https://github.com/gitjayzhen
@software: PyCharm Community Edition
@time: 2017/3/29  13:12
"""
import os
from owl.lib.reporter.logging_porter import LoggingPorter
from owl.lib.file.file_inspector import FileInspector
from owl.lib.file.ConfigReader import ConfigReader
from owl.lib.date.date_formatter import formated_time
'''
创建一个html文件，并返回文件的对象
'''


def html_reporter():
    logger = LoggingPorter()
    fc = FileInspector()
    pro_path = fc.get_project_path()
    boolean = fc.is_has_file("owl-owl.ini")
    if boolean:
        inipath = fc.get_file_abspath()
        cf = ConfigReader(inipath)
    htmlrp_path = cf.get_value("ResultPath", "htmlreportPath")
    htmreportl_abs_path = os.path.join(pro_path, htmlrp_path)
    timecurrent = formated_time("%Y-%m-%d-%H-%M-%S")
    logger.debug("=====创建了一个html文件报告,路径是：："+htmreportl_abs_path)
    file_path = str(htmreportl_abs_path)+timecurrent+"-LDP-TestingRreporter.html"
    try:
        if os.path.exists(file_path):
            html_obj = open(file_path, "a")  # 打开文件   追加
            return html_obj
        else:
            html_obj = open(file_path, "wb+")
            return html_obj
    except Exception as e:
        logger.error("创建html_reporter出现错误"+str(e))


