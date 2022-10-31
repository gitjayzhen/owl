# -*- coding:UTF-8 -*-

'''
Created on 2017年4月28日

@author: jayzhen

这里是测试脚本的一些前置内容
'''
import time
import requests
from requests import exceptions

from framework.services.selenium_service import SeleniumWebDriver
from framework.configs.web_config import WebConfingGetter
from framework.api.browser.selenium_api import SeleniumBaseApi
from framework.utils.date_util.date_formatter import get_formate_time
from framework.utils.reporter.logging_porter import LoggingPorter


class WebDriverController(object):
    """
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

    def get_api_driver(self):
        self.init = SeleniumWebDriver(self.seProperties)
        try:
            resp = requests.get(self.seProperties.baseURL)
            if resp.status_code != 200:
                self.log4py.error("浏览器实例化driver失败，请检查你的被测试服务是否启动或baseURL是否设置正确: {}".format(self.seProperties.baseURL))
        except exceptions.ConnectionError as e:
            self.log4py.error("浏览器实例化driver失败，请检查你的被测试服务是否启动或baseURL是否设置正确: {}".format(self.seProperties.baseURL))
        self.driver = self.init.run_browser()
        if self.driver is None:
            self.log4py.error("浏览器实例化driver失败，请重新检查驱动及启动参数")
            return None
        return SeleniumBaseApi(self.driver, self.seProperties)
    
    def before_suite(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeSuiteStarts = time.time()
        self.log4py.info("======" + begins + "：测试集开始======")

    def after_suite(self):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__afterSuiteStops = time.time()
        self.log4py.info("======" + ends + "：测试集结束======")
        self.log4py.info("======本次测试集运行消耗时间 " + str(self.__afterSuiteStops - self.__beforeSuiteStarts) + " 秒！======")

    def before_class(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeClassStarts = time.time()
        self.log4py.info("======" + str(begins) + "：测试【" + str(self.className) + "】开始======")

    def after_class(self):
        # 如果执行了case，必然已经启动了webdriver，在这里做一次关闭操作
        try:
            self.init.stop_web_driver()
        except Exception as e:
            self.log4py.error("after class with stoping web driver happend error")
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__afterClassStops = time.time()
        self.log4py.info("======" + str(ends) + "：测试【" + str(self.className) + "】结束======")
        self.log4py.info("======本次测试运行消耗时间 " + str(self.__afterClassStops - self.__beforeClassStarts) + " 秒！======")

    def befor_test(self, methodName):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeTestStarts = time.time()
        self.log4py.info("======" + begins + "：案例【" + str(self.className) + "." + methodName+ "】开始======")

    def after_test(self, methodName, isSucceed):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        captureName = ""
        if (isSucceed):
            self.log4py.info("案例 【" + str(self.className) + "." + methodName + "】 运行通过！")
        else:
            dateTime = get_formate_time("-%Y%m%d-%H%M%S%f")
            captureName = self.seProperties.capturePath + str(self.className)+"."+methodName+str(dateTime)+".png"
            self.capture_screenshot(captureName)
            self.log4py.error("案例 【" + str(self.className) + "." + methodName+ "】 运行失败，请查看截图快照：" + captureName)
        self.log4py.info("======" + ends + "：案例【" + str(self.className) + "." + methodName+ "】结束======")
        afterTestStops = time.time()
        self.log4py.info("======本次案例运行消耗时间 " + str(afterTestStops - self.__beforeTestStarts) + " 秒！======")
        return captureName

    def capture(self, name):
        '''
         * 截取屏幕截图并保存到指定路径
         * @param name：保存屏幕截图名称
         * @return 无
         '''
        time.sleep(3)
        dateTime = get_formate_time("-%Y%m%d-%H%M%S-%f")
        captureName = self.seProperties.capturePath + name + dateTime+".png"
        self.capture_screenshot(captureName)
        self.log4py.debug("请查看截图快照：" + captureName)

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

    def operation_check(self, methodName, isSucceed):
        """
         * public method for handle assertions and screenshot.
         * @param isSucceed:if your operation success
         * @throws RuntimeException
        """
        if (isSucceed):
            self.log4py.info("method 【" + methodName + "】 运行通过！")
        else:
            self.log4py.error("method 【" + methodName + "】 运行失败！")
