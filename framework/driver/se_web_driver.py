# -*- coding:UTF-8 -*-

import time
import requests
from requests import exceptions

from framework.services.selenium_service import SeleniumDriverBrowser
from framework.configs.web_config import WebConfingGetter
from framework.api.browser.selenium_api import SeleniumWorkApi
from framework.utils.date_util.date_formatter import get_formate_time
from framework.utils.reporter.logging_porter import LoggingPorter


class WebDriverController(object):
    """这里是测试脚本的一些前置内容
    作为被用例使用的 selenium 操作入口，完成两个工作
    1. 读取参数配置
    2. 实例化 webdriver 对象
    """

    def __init__(self):
        """
        :param clzss: 获取脚本的文件名和class名
        """
        self.driver = None
        # self.className = clzss.__class__.__module__ + "." + clzss.__class__.__name__
        self.className = "Testing"
        self.seProperties = WebConfingGetter().properties
        self.log4py = LoggingPorter()
        self.__beforeSuiteStarts = 0
        self.__beforeClassStarts = 0
        self.__beforeTestStarts = 0
        self.init = None

    def get_driver(self):
        try:
            resp = requests.get(self.seProperties.baseURL)
            if resp.status_code != 200:
                self.log4py.error("浏览器实例化driver失败，请检查你的被测试服务是否启动或baseURL是否设置正确: {}".format(self.seProperties.baseURL))
        except exceptions.ConnectionError as e:
            self.log4py.error("浏览器实例化driver失败，请检查你的被测试服务是否启动或baseURL是否设置正确: {}".format(self.seProperties.baseURL))
        self.init = SeleniumDriverBrowser(self.seProperties)
        self.driver = self.init.init_browser()
        if self.driver is None:
            self.log4py.error("浏览器实例化driver失败，请重新检查驱动及启动参数")
            return None
        return SeleniumWorkApi(self.driver, self.seProperties)
    
    def before_suite(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeSuiteStarts = time.time()
        self.log4py.info("======" + begins + "：测试集开始======")

    def after_suite(self):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.log4py.info("======" + ends + "：测试集结束======")
        self.log4py.info("======本次测试集运行消耗时间 " + str(time.time() - self.__beforeSuiteStarts) + " 秒！======")

    def before_class(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeClassStarts = time.time()
        self.log4py.info("======" + str(begins) + "：测试【" + str(self.className) + "】开始======")

    def after_class(self):
        # 如果执行了case，必然已经启动了webdriver，在这里做一次关闭操作
        try:
            self.init.stop_browser()
        except Exception as e:
            self.log4py.error("after class with stoping web driver happend error")
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.log4py.info("======" + str(ends) + "：测试【" + str(self.className) + "】结束======")
        self.log4py.info("======本次测试运行消耗时间 " + str(time.time() - self.__beforeClassStarts) + " 秒！======")

    def before_test(self, method_name):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeTestStarts = time.time()
        self.log4py.info("======" + begins + "：案例【" + str(self.className) + "." + method_name + "】开始======")

    def after_test(self, method_name, is_succeed):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        capture_name = ""
        if is_succeed:
            self.log4py.info("案例 【" + str(self.className) + "." + method_name + "】 运行通过！")
        else:
            date_time = get_formate_time("-%Y%m%d-%H%M%S%f")
            capture_name = self.seProperties.capturePath + str(self.className) +"." + method_name + str(date_time) + ".png"
            self.capture_screenshot(capture_name)
            self.log4py.error("案例 【" + str(self.className) + "." + method_name + "】 运行失败，请查看截图快照：" + capture_name)
        self.log4py.info("======" + ends + "：案例【" + str(self.className) + "." + method_name + "】结束======")
        self.log4py.info("======本次案例运行消耗时间 " + str(time.time() - self.__beforeTestStarts) + " 秒！======")
        return capture_name

    def capture(self, name):
        """
         * 截取屏幕截图并保存到指定路径
         * @param name：保存屏幕截图名称
         * @return 无
         """
        time.sleep(3)
        date_time = get_formate_time("-%Y%m%d-%H%M%S-%f")
        capture_name = self.seProperties.capturePath + name + date_time + ".png"
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
            self.driver.get_screenshot_as_file(filepath)
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