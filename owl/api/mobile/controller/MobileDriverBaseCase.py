# -*- coding:UTF-8 -*-

"""
Created on 2016年4月28日
@author: jayzhen
"""

import time

from owl.api.mobile.appium_api import AppiumBaseApi
from owl.api.mobile.appium_driver import InitAppiumDriver
from owl.configs.appium_cfg import AppiumConfiger
from owl.lib.date.date_formatter import formated_time
from owl.lib.reporter.logging_porter import LoggingPorter


class MobileDriverBeforeTest(object):

    def __init__(self):
        self.driver = None
        self.className = None
        self.mcg = AppiumConfiger()
        self.log4py = LoggingPorter()
        self.__beforeSuiteStarts = 0
        self.__beforeClassStarts = 0
        self.__beforeTestStarts = 0
        self.init = None

    def get_api_driver(self, sno):
        """
        通过sno获取对应的手机的驱动及其实例化的api对象
        :param sno:
        :return:
        """
        self.init = InitAppiumDriver(self.mcg)
        self.driver = self.init.get_appium_driver(sno)
        if self.driver is None:
            self.log4py.error("appium实例化driver失败，请重新检查驱动及启动参数")
            return None
        return AppiumBaseApi(self.driver, self.mcg.properties)
    
    def before_suite(self):
        begins = formated_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeSuiteStarts = time.time()
        self.log4py.info("======" + begins + "：测试集开始======")

    def after_suite(self):
        ends = formated_time("%Y-%m-%d %H:%M:%S:%f")
        self.__afterSuiteStops = time.time()
        self.log4py.info("======" + ends + "：测试集结束======")
        self.log4py.info("======本次测试集运行消耗时间 " + str(self.__afterSuiteStops - self.__beforeSuiteStarts) + " 秒！======")

    def before_class(self):
        begins = formated_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeClassStarts = time.time()
        self.log4py.info("======" + str(begins) + "：测试【" + str(self.className) + "】开始======")

    def after_class(self):
        # 如果执行了case，必然已经启动了webdriver，在这里做一次关闭操作
        try:
            self.driver.quit()
        except Exception as e:
            self.log4py.error("after class with stoping web driver happend error")
        ends = formated_time("%Y-%m-%d %H:%M:%S:%f")
        self.__afterClassStops = time.time()
        self.log4py.info("======" + str(ends) + "：测试【" + str(self.className) + "】结束======")
        self.log4py.info("======本次测试运行消耗时间 " + str(self.__afterClassStops - self.__beforeClassStarts) + " 秒！======")

    def befor_test(self, methodName):
        begins = formated_time("%Y-%m-%d %H:%M:%S:%f");
        self.__beforeTestStarts = time.time()
        self.log4py.info("======" + begins + "：案例【" + str(self.className) + "." + methodName+ "】开始======")

    def after_test(self, methodName, isSucceed):
        ends = formated_time("%Y-%m-%d %H:%M:%S:%f")
        captureName = ""
        if (isSucceed):
            self.log4py.info("案例 【" + str(self.className) + "." + methodName + "】 运行通过！")
        else:
            dateTime = formated_time("-%Y%m%d-%H%M%S%f")
            captureName = self.seProperties.capture_path + str(self.className) + "." + methodName + str(dateTime) + ".png"
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
        dateTime = formated_time("-%Y%m%d-%H%M%S-%f")
        captureName = self.seProperties.capture_path + name + dateTime + ".png"
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
        if isSucceed:
            self.log4py.info("method 【" + methodName + "】 运行通过！")
        else:
            self.log4py.error("method 【" + methodName + "】 运行失败！")
