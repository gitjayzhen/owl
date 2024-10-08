# -*- coding:UTF-8 -*-

import time

from owl.api.browser.selenium_api import SeleniumWorkApi
from owl.api.browser.selenium_browser import WebBrowser
from owl.configs.selenium_cfg import SeleniumConfiger
from owl.exception.owl_type import BrowserDriverError
from owl.lib.processor.date_processor import get_formate_time
from owl.lib.reporter.log4py import LoggingPorter


class BrowserDriver(object):
    """这里是测试脚本的一些前置内容
    作为被用例使用的 selenium 操作入口，完成两个工作
    1. 读取参数配置
    2. 实例化 webdriver 对象
    """

    def __init__(self, clazz):
        """
        :param clazz: 获取脚本的文件名和class名
        """
        self.log4py = LoggingPorter()
        self.className = clazz.__class__.__module__ + "." + clazz.__class__.__name__
        self.selenium_props = None
        self.driver_instance = None
        self.se_api = None
        self.__beforeSuiteStart = 0
        self.__beforeClassStart = 0
        self.__beforeTestStart = 0

    def init_driver(self):
        return self.get_driver()

    def get_driver(self):
        try:
            self.selenium_props = SeleniumConfiger().properties
            self.driver_instance = WebBrowser(self.selenium_props).start_browser()
            self.se_api = SeleniumWorkApi(self.driver_instance, self.selenium_props)
            return self.se_api
        except BrowserDriverError as e:
            self.log4py.error(str(e))
            return None

    def before_suite(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeSuiteStart = time.time()
        self.log4py.info("======" + begins + "：测试集开始======")

    def after_suite(self):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.log4py.info("======" + ends + "：测试集结束======")
        self.log4py.info("======本次测试集运行消耗时间 " + str(time.time() - self.__beforeSuiteStart) + " 秒！======")

    def before_class(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeClassStart = time.time()
        self.log4py.info("======" + str(begins) + "：测试【" + str(self.className) + "】开始======")

    def after_class(self):
        """
        如果执行了case，必然已经启动了webdriver，在这里做一次关闭操作
        """
        self.se_api.stop_web_driver()
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.log4py.info("======" + str(ends) + "：测试【" + str(self.className) + "】结束======")
        self.log4py.info("======本次测试运行消耗时间 " + str(time.time() - self.__beforeClassStart) + " 秒！======")

    def before_test(self, method_name):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeTestStart = time.time()
        self.log4py.info("======" + begins + "：案例【" + str(self.className) + "." + method_name + "】开始======")

    def after_test(self, method_name, is_succeed):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        capture_name = ""
        if is_succeed:
            self.log4py.info("案例 【" + str(self.className) + "." + method_name + "】 运行通过！")
        else:
            date_time = get_formate_time("-%Y%m%d-%H%M%S%f")
            capture_name = self.selenium_props.capture_path + str(self.className) + "." + method_name + str(date_time) + ".png"
            self.capture_screenshot(capture_name)
            self.log4py.error("案例 【" + str(self.className) + "." + method_name + "】 运行失败，请查看截图快照：" + capture_name)
        self.log4py.info("======" + ends + "：案例【" + str(self.className) + "." + method_name + "】结束======")
        self.log4py.info("======本次案例运行消耗时间 " + str(time.time() - self.__beforeTestStart) + " 秒！======")
        return capture_name

    def capture(self, name):
        """
         * 截取屏幕截图并保存到指定路径
         * @param name：保存屏幕截图名称
         * @return 无
         """
        time.sleep(3)
        date_time = get_formate_time("-%Y%m%d-%H%M%S-%f")
        capture_name = self.selenium_props.capture_path + name + date_time + ".png"
        self.capture_screenshot(capture_name)
        self.log4py.debug("请查看截图快照：" + capture_name)

    def capture_screenshot(self, filepath):
        """
        * 截取屏幕截图并保存到指定路径
        * @param filepath:保存屏幕截图完整文件名称及路径
        * @return 无
        :param filepath:
        :return:
        """
        try:
            self.driver_instance.get_screenshot_as_file(filepath)
        except Exception as e:
            self.log4py.error("保存屏幕截图失败，失败信息："+str(e))

    def operation_check(self, method_name, is_succeed):
        """
         * public method for handle assertions and screenshot.
         * @param isSucceed:if your operation success
         * @throws RuntimeException
        """
        if is_succeed:
            self.log4py.info("method 【" + method_name + "】 运行通过！")
        else:
            self.log4py.error("method 【" + method_name + "】 运行失败！")
