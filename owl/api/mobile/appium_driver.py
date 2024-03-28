# -*- encoding: utf-8 -*-
"""
@version: v1.0
@author: jayzhen
@time: 2023/8/3  17:22 当前只能是一个设备
@TODO 多线程并发执行脚本时，需要将端口、手机设备的关联做好;多个设备时desired_capabilities属性只能是一个设备
"""
import re
import subprocess
import time
from urllib.error import URLError

from appium import webdriver
from selenium.webdriver.remote.errorhandler import ErrorHandler

from owl.api.mobile.appium_api import AppiumWorkApi
from owl.api.mobile.adb.adb import AndroidDebugBridge
from owl.exception.server_type import AppiumServiceNotRunningException
from owl.lib.common import Utils
from owl.lib.date.date_formatter import get_formate_time
from owl.lib.file.config_resolver import ConfigControl
from owl.lib.reporter.logging_porter import LoggingPorter


class InitAppiumDriver(object):

    def __init__(self, props_obj):
        self.log4py = LoggingPorter()
        self.run_cfg = props_obj
        self.android = AndroidDebugBridge()
        self.run_data = None
        self.driver = None
        self.className = None
        self.log4py = LoggingPorter()
        self.__beforeSuiteStarts = 0
        self.__beforeClassStarts = 0
        self.__beforeTestStarts = 0
        self.init = None

    def __get_device_capabilities(self, sno):
        device_info = {"udid": sno}
        try:
            result = subprocess.Popen("adb -s %s shell getprop" % sno, shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).stdout.readlines()
            for res in result:
                res = res.decode()
                if re.search(r"ro\.build\.version\.release", res):
                    device_info["platformVersion"] = (res.split(': ')[-1].strip())[1:-1]
                elif re.search(r"ro\.product\.model", res):
                    device_info["deviceName"] = (res.split(': ')[-1].strip())[1:-1]
                if "platformVersion" in device_info.keys() and "deviceName" in device_info.keys():
                    break
        except Exception as e:
            self.log4py.error("获取手机信息时出错 :" + str(e))
            return None
        desired_caps_conf = self.run_cfg.get_desired_caps_conf()
        device_info.update(desired_caps_conf)
        return device_info

    def __get_appium_server_port(self, sno):
        """
        这里读取启动服务时生成的那个ini配置文件，读取其中sno对应的状态及服务的port
        """
        server_mark = ConfigControl(self.run_cfg.properties.appiumService)
        port = server_mark.get_value(sno, sno)
        self.log4py.info("获取到 {} 设备对应的appium服务端口 {}".format(sno, port))
        if not Utils.is_port_used(port):
            info = "设备号 {} 对应的 appium 服务没有启动".format(sno)
            self.log4py.debug(info)
            raise AppiumServiceNotRunningException(info)
        return port

    def __require_install_apk(self, sno):
        """
        在实例appium driver前，进行设备的操作：安装、卸载
        :param sno:
        :return:
        """
        self.android.set_serial_num(sno)
        self.run_data = self.run_cfg.get_run_conf()
        if int(self.run_data["is_first"]) == 0:
            if self.android.is_install_app(self.run_data["pkg_name"]):
                self.android.do_uninstall_app(self.run_data["pkg_name"])
                self.log4py.info("对测试设备进行卸载应用操作：{}".format(self.run_data["pkg_name"]))
            res = self.android.do_install_app(self.run_data["apk_file_path"], self.run_data["pkg_name"])
            self.log4py.info(
                "重新安装应用{} : {} : {}".format(self.run_data["apk_file_path"], self.run_data["pkg_name"], res))
        elif int(self.run_data["is_first"]) == 1:
            self.log4py.info("非首次执行，可以直接进行正常用例操作")

    def get_appium_driver(self, sno):
        desired_caps = self.__get_device_capabilities(sno)
        self.__require_install_apk(desired_caps['udid'])
        port = self.__get_appium_server_port(desired_caps["udid"])
        url = 'http://127.0.0.1:%s/wd/hub' % (port.strip())
        num = 0
        driver = None
        while num <= 5:
            try:
                driver = webdriver.Remote(url, desired_caps)
            except URLError as e:
                self.log4py.error("连接appium服务，实例化driver时出错，尝试重连...({})".format(num))
                num = num + 1
                continue
            except ErrorHandler as e2:
                self.log4py.error("appium {} 服务 404, 请手动检查".format(url))
                raise AppiumServiceNotRunningException(url)
            if self.run_data["wait_activity"] is not None:
                driver.wait_activity(self.run_data["wait_activity"], 10)
            else:
                driver.implicitly_wait(10)
            self.log4py.info("webdriver连接信息：{}：{}".format(url, str(desired_caps)))
            break
        api = AppiumWorkApi(driver, self.run_cfg.properties)
        return api

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
        return AppiumWorkApi(self.driver, self.mcg.properties)

    def before_suite(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeSuiteStarts = time.time()
        self.log4py.info("======" + begins + "：测试集开始======")

    def after_suite(self):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__afterSuiteStops = time.time()
        self.log4py.info("======" + ends + "：测试集结束======")
        self.log4py.info(
            "======本次测试集运行消耗时间 " + str(self.__afterSuiteStops - self.__beforeSuiteStarts) + " 秒！======")

    def before_class(self):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__beforeClassStarts = time.time()
        self.log4py.info("======" + str(begins) + "：测试【" + str(self.className) + "】开始======")

    def after_class(self):
        # 如果执行了case，必然已经启动了webdriver，在这里做一次关闭操作
        try:
            self.driver.quit()
        except Exception as e:
            self.log4py.error("after class with stoping web driver happend error")
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        self.__afterClassStops = time.time()
        self.log4py.info("======" + str(ends) + "：测试【" + str(self.className) + "】结束======")
        self.log4py.info(
            "======本次测试运行消耗时间 " + str(self.__afterClassStops - self.__beforeClassStarts) + " 秒！======")

    def befor_test(self, methodName):
        begins = get_formate_time("%Y-%m-%d %H:%M:%S:%f");
        self.__beforeTestStarts = time.time()
        self.log4py.info("======" + begins + "：案例【" + str(self.className) + "." + methodName + "】开始======")

    def after_test(self, methodName, isSucceed):
        ends = get_formate_time("%Y-%m-%d %H:%M:%S:%f")
        captureName = ""
        if (isSucceed):
            self.log4py.info("案例 【" + str(self.className) + "." + methodName + "】 运行通过！")
        else:
            dateTime = get_formate_time("-%Y%m%d-%H%M%S%f")
            captureName = self.seProperties.capture_path + str(self.className) + "." + methodName + str(
                dateTime) + ".png"
            self.capture_screenshot(captureName)
            self.log4py.error(
                "案例 【" + str(self.className) + "." + methodName + "】 运行失败，请查看截图快照：" + captureName)
        self.log4py.info("======" + ends + "：案例【" + str(self.className) + "." + methodName + "】结束======")
        afterTestStops = time.time()
        self.log4py.info("======本次案例运行消耗时间 " + str(afterTestStops - self.__beforeTestStarts) + " 秒！======")
        return captureName

    def capture(self, name):
        """
        * 截取屏幕截图并保存到指定路径
        * @param name：保存屏幕截图名称
        * @return 无
        """
        time.sleep(3)
        dateTime = get_formate_time("-%Y%m%d-%H%M%S-%f")
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
            self.log4py.error("保存屏幕截图失败，失败信息：" + str(e))

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
